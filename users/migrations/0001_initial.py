# Generated by Django 3.2.4 on 2021-06-22 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=30)),
                ('address', models.CharField(max_length=1000)),
                ('telephone', models.IntegerField()),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
