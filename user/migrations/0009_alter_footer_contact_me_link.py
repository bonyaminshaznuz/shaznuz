# Generated by Django 5.1.6 on 2025-02-11 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_footer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footer',
            name='contact_me_link',
            field=models.CharField(max_length=200),
        ),
    ]
