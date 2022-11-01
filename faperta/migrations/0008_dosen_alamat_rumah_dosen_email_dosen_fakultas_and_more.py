# Generated by Django 4.1.1 on 2022-10-05 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faperta', '0007_remove_dosen_alamat_rumah_remove_dosen_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dosen',
            name='alamat_rumah',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dosen',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dosen',
            name='fakultas',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dosen',
            name='mahasiswa_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='faperta.mahasiswa'),
        ),
        migrations.AddField(
            model_name='dosen',
            name='nama',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dosen',
            name='photo',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dosen',
            name='prodi',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dosen',
            name='tanggal_lahir',
            field=models.DateField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='dosen',
            name='tendik_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='faperta.tendik'),
        ),
    ]