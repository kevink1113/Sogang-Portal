# Generated by Django 4.2.1 on 2023-05-12 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(max_length=10, null=True)),
                ('semester', models.IntegerField()),
                ('name', models.CharField(max_length=30, null=True)),
                ('day', models.IntegerField()),
                ('start_time', models.TimeField(null=True)),
                ('end_time', models.TimeField(null=True)),
                ('classroom', models.CharField(default='', max_length=15)),
                ('advisor', models.CharField(max_length=30)),
                ('major', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Takes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('middle_grade', models.FloatField(null=True)),
                ('final_grade', models.FloatField(null=True)),
                ('real', models.BooleanField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pybo.course')),
            ],
        ),
    ]
