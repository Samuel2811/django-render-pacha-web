# Generated by Django 4.2.4 on 2024-07-09 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pachamodel', '0003_usuario_brillo'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='diariego',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='usuario',
            name='horariego',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
