# Generated by Django 4.1.1 on 2022-10-05 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dosen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NIP', models.CharField(max_length=50)),
                ('nama', models.CharField(max_length=50)),
                ('tanggal_lahir', models.CharField(max_length=50)),
                ('photo', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('fakultas', models.CharField(max_length=50)),
                ('prodi', models.CharField(max_length=50)),
                ('alamat_rumah', models.CharField(max_length=50)),
            ],
        ),
    ]