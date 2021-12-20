# Generated by Django 4.0 on 2021-12-19 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estate',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='images/')),
                ('estate', models.ManyToManyField(to='estateApp.Estate')),
            ],
        ),
        migrations.CreateModel(
            name='LandPlot',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.FileField(upload_to='files/')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='estateApp.person')),
            ],
        ),
        migrations.AddField(
            model_name='estate',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='estateApp.status'),
        ),
    ]
