# Generated by Django 5.2.1 on 2025-06-08 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Libro', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='id',
        ),
        migrations.AddField(
            model_name='libro',
            name='libro_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
