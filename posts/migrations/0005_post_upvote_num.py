# Generated by Django 4.2.1 on 2023-05-26 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_remove_post_iine_post_upvote_remove_post_view_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='upvote_num',
            field=models.IntegerField(default=0),
        ),
    ]
