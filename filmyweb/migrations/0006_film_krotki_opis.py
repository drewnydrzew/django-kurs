# Generated by Django 3.1.1 on 2020-09-26 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0005_auto_20200925_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='krotki_opis',
            field=models.CharField(max_length=195, null=True),
        ),
    ]
