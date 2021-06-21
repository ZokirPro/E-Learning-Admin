# Generated by Django 3.1.1 on 2021-06-21 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('img', models.ImageField(upload_to='groups/')),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'groups',
            },
        ),
        migrations.CreateModel(
            name='Student_Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groups.group')),
            ],
            options={
                'db_table': 'student_groups',
            },
        ),
    ]
