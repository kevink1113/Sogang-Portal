# Generated by Django 4.2.1 on 2023-05-11 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='major',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_id',
            field=models.CharField(max_length=15, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Major',
        ),
    ]
