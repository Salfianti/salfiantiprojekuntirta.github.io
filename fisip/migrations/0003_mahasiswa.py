# Generated by Django 4.1.1 on 2022-10-05 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fisip', '0002_tendik_dosen_tendik_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NIM', models.IntegerField(null=True)),
                ('nama', models.CharField(max_length=50)),
                ('tanggal_lahir', models.DateField(max_length=50)),
                ('photo', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('fakultas', models.CharField(max_length=50)),
                ('prodi', models.CharField(max_length=50)),
            ],
        ),
    ]
