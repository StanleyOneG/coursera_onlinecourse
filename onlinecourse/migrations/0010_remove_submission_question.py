# Generated by Django 3.1.3 on 2022-12-15 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0009_submission_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='question',
        ),
    ]