# Generated by Django 4.2.1 on 2023-06-25 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bancodados', '0002_usuario_delete_usuarios'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='idade',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
