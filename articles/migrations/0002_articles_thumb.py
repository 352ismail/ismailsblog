# Generated by Django 4.2.5 on 2023-10-06 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
