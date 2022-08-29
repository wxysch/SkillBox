# Generated by Django 4.1 on 2022-08-29 03:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Язык',
                'verbose_name_plural': 'Языки',
            },
        ),
        migrations.RemoveField(
            model_name='course',
            name='language',
        ),
        migrations.AddField(
            model_name='course',
            name='languages',
            field=models.ForeignKey(default=1, max_length=255, on_delete=django.db.models.deletion.CASCADE, to='courses.language'),
            preserve_default=False,
        ),
    ]
