# Generated by Django 4.0.4 on 2022-05-13 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchq',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='searchq',
            name='score',
            field=models.IntegerField(null=True),
        ),
    ]
