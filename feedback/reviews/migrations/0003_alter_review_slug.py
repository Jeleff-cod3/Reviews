# Generated by Django 5.1.6 on 2025-03-11 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_review_slug_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
