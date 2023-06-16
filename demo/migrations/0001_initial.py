# Generated by Django 4.0.4 on 2022-05-08 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=200)),
                ('part_of_speech', models.CharField(max_length=100)),
                ('definition', models.TextField()),
                ('example', models.TextField()),
            ],
        ),
    ]
