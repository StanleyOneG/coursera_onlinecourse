# Generated by Django 3.1.3 on 2022-12-14 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0007_auto_20221214_0602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='is_correct',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=9, verbose_name='Is this correct answer?'),
        ),
    ]