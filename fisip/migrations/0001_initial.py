# Generated by Django 4.1.1 on 2022-10-05 12:50

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
                ('NIP', models.IntegerField(null=True)),
                ('nama', models.CharField(max_length=50, null=True)),
                ('tanggal_lahir', models.DateField(max_length=50, null=True)),
                ('photo', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('fakultas', models.CharField(max_length=50, null=True)),
                ('prodi', models.CharField(max_length=50, null=True)),
                ('alamat_rumah', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
