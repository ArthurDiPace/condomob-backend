# Generated by Django 4.2.13 on 2024-06-14 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_arquivohash_delete_arquivo'),
    ]

    operations = [
        migrations.AddField(
            model_name='arquivohash',
            name='usuario',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
