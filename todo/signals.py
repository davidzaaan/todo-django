from django import dispatch
from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch.dispatcher import receiver
from .models import UserTaskProfile
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings


def create_user(sender, instance, created, **kwargs):
    print('post save signal triggered')
    if created:
        user = instance
        profile = UserTaskProfile.objects.create(user=user, name=user.first_name, email=user.email, password=user.password)

        try:
            send_mail(
                    'Welcome to ToDo',
                    'Glad to have you here. You can add now new tasks to your timeline',
                    settings.EMAIL_HOST_USER,
                    [profile.email],
                    fail_silently=False
                )
        except:
            pass


def delete_user(sender, instance, **kwargs):
    try:
        user = User.objects.get(username=instance.name.lower())
        user.delete()
        print('trying to delete user :(')
    except:
        pass


post_save.connect(create_user, sender=User)
post_delete.connect(delete_user, sender=UserTaskProfile)
