# Generated by Django 5.1.6 on 2025-02-11 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_heroinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroinfo',
            name='download_cv_button',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='heroinfo',
            name='hireme_link',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]
