# Generated by Django 3.1.1 on 2020-09-27 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0016_comments_aut'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='komentarz',
            field=models.TextField(default='', max_length=500),
        ),
    ]
