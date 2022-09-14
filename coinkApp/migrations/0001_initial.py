# Generated by Django 4.1.1 on 2022-09-13 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserBasic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=180)),
                ('email', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
    ]
