# Generated by Django 4.1.1 on 2022-10-05 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
        migrations.CreateModel(
            name='Tendik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NIP', models.IntegerField(null=True)),
                ('nama', models.CharField(max_length=50)),
                ('tanggal_lahir', models.DateField(max_length=50)),
                ('photo', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('unit', models.CharField(max_length=50)),
                ('alamat_rumah', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Dosen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NIP', models.IntegerField(null=True)),
                ('nama', models.CharField(max_length=50, null=True)),
                ('tanggal_lahir', models.DateField(max_length=50, null=True)),
                ('photo', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('fakultas', models.CharField(max_length=50, null=True)),
                ('prodi', models.CharField(max_length=50, null=True)),
                ('alamat_rumah', models.CharField(max_length=50, null=True)),
                ('mahasiswa_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fh.mahasiswa')),
                ('tendik_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fh.tendik')),
            ],
        ),
    ]
