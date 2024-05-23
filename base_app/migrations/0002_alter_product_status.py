# Generated by Django 5.0.6 on 2024-05-21 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('Available', 'Available'), ('Out of Stock', 'Out of Stock')], default='Available', max_length=240),
        ),
    ]