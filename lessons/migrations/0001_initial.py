# Generated by Django 3.1.1 on 2021-06-21 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('library', '0003_auto_20210621_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('img', models.ImageField(upload_to='lessons/')),
                ('publish', models.BooleanField()),
            ],
            options={
                'db_table': 'lessons',
            },
        ),
        migrations.CreateModel(
            name='Lesson_Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('sort', models.IntegerField()),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.lesson')),
            ],
            options={
                'db_table': 'lesson_plans',
            },
        ),
        migrations.CreateModel(
            name='Student_and_Lessons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress', models.FloatField()),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.lesson')),
            ],
            options={
                'db_table': 'student_and_lessons',
            },
        ),
        migrations.CreateModel(
            name='Plan_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True)),
                ('sort', models.IntegerField()),
                ('material', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.educational_material')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lessons.lesson_plan')),
            ],
            options={
                'db_table': 'plan_details',
            },
        ),
    ]
