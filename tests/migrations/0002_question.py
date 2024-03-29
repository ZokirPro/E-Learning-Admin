# Generated by Django 3.1.1 on 2021-06-21 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('type_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tests.type_questions')),
            ],
            options={
                'db_table': 'questions',
            },
        ),
    ]
