# Generated by Django 4.1.1 on 2022-10-05 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faperta', '0008_dosen_alamat_rumah_dosen_email_dosen_fakultas_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dosen',
            name='NIP',
            field=models.IntegerField(max_length=50, null=True),
        ),
    ]