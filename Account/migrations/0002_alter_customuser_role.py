# Generated by Django 5.0.7 on 2024-07-11 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('trainee', 'Trainee'), ('member', 'Member'), ('admin', 'Admin')], max_length=10),
        ),
    ]
