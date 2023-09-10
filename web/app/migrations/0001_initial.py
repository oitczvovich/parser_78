# Generated by Django 4.2.5 on 2023-09-09 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('post_url', models.CharField(max_length=256)),
                ('post_title', models.CharField(max_length=256)),
                ('date_create', models.CharField(max_length=100)),
                ('post_text', models.TextField()),
            ],
        ),
    ]