# Generated by Django 3.2.2 on 2021-05-31 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='review_user',
            new_name='profile',
        ),
    ]
