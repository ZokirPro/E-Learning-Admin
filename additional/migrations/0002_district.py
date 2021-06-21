# Generated by Django 3.1.1 on 2021-06-21 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('additional', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('code', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='additional.region')),
            ],
            options={
                'db_table': 'districts',
            },
        ),
    ]
