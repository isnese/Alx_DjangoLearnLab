# Generated by Django 4.2.14 on 2024-09-09 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publication_date',
            new_name='published_date',
        ),
    ]
