# Generated by Django 4.0.5 on 2022-06-25 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_advertisement_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='picture',
            field=models.ImageField(upload_to='pictures', verbose_name='Фото'),
        ),
    ]
