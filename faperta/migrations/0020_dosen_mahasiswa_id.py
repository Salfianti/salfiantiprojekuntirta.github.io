# Generated by Django 4.1.1 on 2022-10-05 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('faperta', '0019_dosen_tendik_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='dosen',
            name='mahasiswa_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='faperta.mahasiswa'),
        ),
    ]
