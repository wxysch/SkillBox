# Generated by Django 4.1 on 2022-09-17 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_remove_course_languages_course_languages'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField(default=0, verbose_name='Значение')),
            ],
            options={
                'verbose_name': 'Звезда рейтинга',
                'verbose_name_plural': 'Звёзды рейтинга',
            },
        ),
    ]
