# Generated by Django 3.1.1 on 2020-09-26 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0007_auto_20200926_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='krotki_opis',
            field=models.TextField(default='', max_length=195, null=True),
        ),
        migrations.AlterField(
            model_name='film',
            name='opis',
            field=models.TextField(default=''),
        ),
    ]
