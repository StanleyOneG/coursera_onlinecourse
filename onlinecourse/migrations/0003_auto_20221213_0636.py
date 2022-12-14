# Generated by Django 3.1.3 on 2022-12-13 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20221212_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='course',
            field=models.ManyToManyField(to='onlinecourse.Course'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='indicator',
            field=models.CharField(choices=[('Correct', True), ('Incorrect', False)], max_length=9),
        ),
        migrations.AlterField(
            model_name='question',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='onlinecourse.lesson', verbose_name='Lesson name'),
        ),
    ]
