# Generated by Django 2.2.7 on 2020-09-02 06:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20200902_0554'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='buy',
            new_name='price',
        ),
    ]
