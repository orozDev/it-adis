# Generated by Django 3.2.12 on 2022-03-17 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursesrelease',
            name='image',
            field=models.ImageField(null=True, upload_to='courses_release/', verbose_name='Заголовочная кортина'),
        ),
    ]
