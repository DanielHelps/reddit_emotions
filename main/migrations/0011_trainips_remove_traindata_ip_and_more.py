# Generated by Django 4.0.4 on 2022-06-03 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_traindata_user_traindata_ip'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainIps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='traindata',
            name='ip',
        ),
        migrations.AlterField(
            model_name='traindata',
            name='positive_score',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='traindata',
            name='times_answered',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='traindata',
            name='train_ips',
            field=models.ManyToManyField(to='main.trainips'),
        ),
    ]
