# Generated by Django 5.1.6 on 2025-02-11 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='favicon',
            field=models.FileField(blank=True, help_text='Upload an SVG file', null=True, upload_to='favicons/'),
        ),
    ]
