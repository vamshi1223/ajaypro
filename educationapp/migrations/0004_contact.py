# Generated by Django 5.0.7 on 2024-08-09 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educationapp', '0003_remove_feedback_phonenumber_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('phonenumber', models.CharField()),
                ('email', models.EmailField(default='default@example.com', max_length=254)),
                ('yourmessage', models.TextField()),
            ],
        ),
    ]
