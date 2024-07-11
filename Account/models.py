from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    TRAINEE = 'trainee'
    MEMBER = 'member'
    ADMIN = 'admin'

    ROLE_CHOICES = [
        (TRAINEE, 'Trainee'),
        (MEMBER, 'Member'),
        (ADMIN, 'Admin'),
    ]

    email = models.EmailField(unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    @property
    def is_admin(self):
        return self.role == self.ADMIN

    class Meta:
        permissions = [
            ("view_trainee_content", "Can view trainee content"),
            ("edit_trainee_content", "Can edit trainee content"),
            ("delete_trainee_content", "Can delete trainee content"),
            ("add_trainee_content", "Can add trainee content"),
            ("view_member_content", "Can view member content"),
            ("edit_member_content", "Can edit member content"),
            ("delete_member_content", "Can delete member content"),
            ("add_member_content", "Can add member content"),
            ("view_admin_content", "Can view admin content"),
            ("edit_admin_content", "Can edit admin content"),
            ("delete_admin_content", "Can delete admin content"),
            ("add_admin_content", "Can add admin content"),
        ]


class TraineeProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='trainee_profile')
    bio = models.TextField(blank=True)
    certifications = models.CharField(max_length=100, blank=True)
    specialization = models.CharField(max_length=100, blank=True)
    permissions = models.ManyToManyField('auth.Permission', blank=True)

    def __str__(self):
        return self.user.username

class MemberProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='member_profile')
    membership_date = models.DateField(auto_now_add=True)
    membership_type = models.CharField(max_length=50)
    permissions = models.ManyToManyField('auth.Permission', blank=True)

    def __str__(self):
        return self.user.username

class AdminProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='admin_profile')
    role = models.CharField(max_length=50)
    permissions = models.ManyToManyField('auth.Permission', blank=True)

    def __str__(self):
        return self.user.username