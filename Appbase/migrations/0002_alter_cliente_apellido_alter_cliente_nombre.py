# Generated by Django 5.0.6 on 2024-07-03 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appbase', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='apellido',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=20),
        ),
    ]