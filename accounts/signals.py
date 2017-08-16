from django.contrib.auth.models import Group, Permission
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from .models import Manager, UserProfile, Secretary


def generate_permissions(sending_instance, user):
    custom_permissions = {
        'Manager': [
            'can_view_reports',
        ],
        'Secretary': [
            'can_book_users',
            'add_bookedroom',
            'change_bookedroom'
        ]
    }

    permissions_list = []

    if sending_instance in custom_permissions:
        new_sending_instance = '%s%s' % (sending_instance,  's')
        default_perms = custom_permissions[sending_instance]

        for perm in default_perms:
            p = Permission.objects.get(codename=perm)
            permissions_list.append(p)

        try:
            group = Group.objects.get(name=new_sending_instance)

        except Group.DoesNotExist:
            Group.objects.create(
                name=new_sending_instance
            )
            group = Group.objects.get(name=new_sending_instance)

        for perm in permissions_list:
            group.permissions.add(perm)
        group.user_set.add(user)
        user.is_staff = True
        user.save()


def assign_permissions(sender, instance, **kwargs):
    user = instance.user
    sending_instance = instance.__class__.__name__
    return generate_permissions(sending_instance, user)


@receiver(pre_save, sender=UserProfile)
def create_userprofile_slug(sender, instance, **kwargs):
    user = instance.username
    instance.slug = user


post_save.connect(assign_permissions, Manager)
post_save.connect(assign_permissions, Secretary)
