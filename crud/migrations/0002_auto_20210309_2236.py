# Generated by Django 3.1.7 on 2021-03-09 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crud',
            name='deskripsi',
            field=models.CharField(max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crud',
            name='dosen',
            field=models.CharField( max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='crud',
            name='jumlah_sks',
            field=models.CharField( max_length=40),
            preserve_default=False,
        ),
    ]