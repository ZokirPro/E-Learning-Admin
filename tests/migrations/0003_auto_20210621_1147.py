# Generated by Django 3.1.1 on 2021-06-21 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0002_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='type_id',
            new_name='type',
        ),
    ]