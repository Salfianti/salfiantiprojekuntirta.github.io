# Generated by Django 4.1.1 on 2022-10-05 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faperta', '0014_dosen_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='dosen',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
