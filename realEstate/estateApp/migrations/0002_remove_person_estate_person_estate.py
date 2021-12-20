# Generated by Django 4.0 on 2021-12-20 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estateApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='estate',
        ),
        migrations.AddField(
            model_name='person',
            name='estate',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='estateApp.estate'),
            preserve_default=False,
        ),
    ]
