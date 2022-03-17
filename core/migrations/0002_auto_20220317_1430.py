# Generated by Django 3.2.12 on 2022-03-17 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Заметки')),
                ('question', models.CharField(max_length=1000, verbose_name='Вопрос')),
                ('answer', models.TextField(verbose_name='Ответ (Контетн)')),
            ],
            options={
                'verbose_name': 'часто задаваемый вопрос',
                'verbose_name_plural': 'часто задаваемые вопросы',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ['-updated_at'], 'verbose_name': 'группа', 'verbose_name_plural': 'группы'},
        ),
        migrations.AlterModelOptions(
            name='professions',
            options={'ordering': ['-updated_at'], 'verbose_name': 'профессия', 'verbose_name_plural': 'профессии'},
        ),
        migrations.AddField(
            model_name='pages',
            name='css_file',
            field=models.FileField(blank=True, null=True, upload_to='css_files/', verbose_name='CSS файл'),
        ),
        migrations.AddField(
            model_name='posts',
            name='css_file',
            field=models.FileField(blank=True, null=True, upload_to='css_files/', verbose_name='CSS файл'),
        ),
        migrations.AlterField(
            model_name='courses',
            name='css_file',
            field=models.FileField(blank=True, null=True, upload_to='css_files/', verbose_name='CSS файл'),
        ),
    ]
