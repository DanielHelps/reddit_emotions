# Generated by Django 4.0.4 on 2022-07-15 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_top_100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='top_100',
            name='top_date',
        ),
        migrations.RemoveField(
            model_name='top_100',
            name='top_pos_neg',
        ),
        migrations.AddField(
            model_name='top_100',
            name='neg_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='top_100',
            name='pos_date',
            field=models.DateField(null=True),
        ),
    ]
