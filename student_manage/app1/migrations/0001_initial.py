# Generated by Django 5.0.4 on 2024-04-16 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.EmailField(max_length=40, null=True)),
                ('password', models.CharField(max_length=60, null=True)),
            ],
        ),
    ]
