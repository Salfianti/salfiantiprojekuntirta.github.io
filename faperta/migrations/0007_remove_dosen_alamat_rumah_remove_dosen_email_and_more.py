# Generated by Django 4.1.1 on 2022-10-05 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faperta', '0006_dosen_mahasiswa_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dosen',
            name='alamat_rumah',
        ),
        migrations.RemoveField(
            model_name='dosen',
            name='email',
        ),
        migrations.RemoveField(
            model_name='dosen',
            name='fakultas',
        ),
        migrations.RemoveField(
            model_name='dosen',
            name='mahasiswa_id',
        ),
        migrations.RemoveField(
            model_name='dosen',
            name='nama',
        ),
        migrations.RemoveField(
            model_name='dosen',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='dosen',
            name='prodi',
        ),
        migrations.RemoveField(
            model_name='dosen',
            name='tanggal_lahir',
        ),
        migrations.RemoveField(
            model_name='dosen',
            name='tendik_id',
        ),
        migrations.AlterField(
            model_name='dosen',
            name='NIP',
            field=models.IntegerField(max_length=50),
        ),
    ]
