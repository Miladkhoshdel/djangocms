# Generated by Django 4.0.4 on 2022-05-04 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('key_field', models.CharField(max_length=254, verbose_name='Key')),
                ('value_field', models.CharField(max_length=254, verbose_name='Value')),
            ],
            options={
                'verbose_name': 'Website Config',
                'verbose_name_plural': 'Website Configs',
                'db_table': 'WebsiteConfig',
            },
        ),
    ]
