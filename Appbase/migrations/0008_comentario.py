# Generated by Django 5.0.6 on 2024-07-04 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Appbase', '0007_delete_cliente_alter_libro_apellido_del_duenio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=100)),
                ('texto', models.TextField()),
                ('fecha_comentario', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
