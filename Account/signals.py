from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from .models import CustomUser, TraineeProfile, MemberProfile, AdminProfile

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = None
        permissions = []
        if instance.role == CustomUser.TRAINEE:
            profile = TraineeProfile.objects.create(user=instance)
            permissions = [
                'view_trainee_content',
                'edit_trainee_content',
                'delete_trainee_content',
                'add_trainee_content'
            ]
        elif instance.role == CustomUser.MEMBER:
            profile = MemberProfile.objects.create(user=instance)
            permissions = [
                'view_member_content',
                'edit_member_content',
                'delete_member_content',
                'add_member_content'
            ]
        elif instance.role == CustomUser.ADMIN:
            profile = AdminProfile.objects.create(user=instance)
            permissions = [
                'view_admin_content',
                'edit_admin_content',
                'delete_admin_content',
                'add_admin_content'
            ]

        if profile:
            assign_permissions(instance, permissions)

def assign_permissions(user, permissions):
    # Clear existing permissions
    user.user_permissions.clear()
    # Set new permissions
    permission_objects = Permission.objects.filter(codename__in=permissions)
    user.user_permissions.set(permission_objects)
    user.save()

@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.role == CustomUser.TRAINEE:
        TraineeProfile.objects.get_or_create(user=instance)
        instance.trainee_profile.save()
    elif instance.role == CustomUser.MEMBER:
        MemberProfile.objects.get_or_create(user=instance)
        instance.member_profile.save()
    elif instance.role == CustomUser.ADMIN:
        AdminProfile.objects.get_or_create(user=instance)
        instance.admin_profile.save()

