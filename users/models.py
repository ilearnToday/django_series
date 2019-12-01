from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
import os
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_image.path)

        if img.height > 300 and img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_image.path)


@receiver(models.signals.post_delete, sender=Profile)
def auto_delete_profile_img_on_delete(sender, instance, **kwargs):
    if instance.profile_image and instance.profile_image.name != 'default.jpg':
        if os.path.isfile(instance.profile_image.path):
            os.remove(instance.profile_image.path)


@receiver(models.signals.pre_save, sender=Profile)
def auto_delete_old_profile_img_on_update(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_img = sender.objects.get(pk=instance.pk).profile_image
        if old_img.name == 'default.jpg':
            return False
    except sender.DoesNotExist:
        return False
    new_img = instance.profile_image
    if not old_img == new_img:
        if os.path.isfile(old_img.path):
            os.remove(old_img.path)

