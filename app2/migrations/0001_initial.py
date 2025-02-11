# Generated by Django 5.1.6 on 2025-02-11 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('context', models.TextField(blank=True)),
                ('created_ed', models.DateTimeField(auto_now_add=True)),
                ('updated_ed', models.DateTimeField(auto_now=True)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('is_bool', models.BooleanField(default=True)),
            ],
        ),
    ]
