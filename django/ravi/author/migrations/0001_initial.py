# Generated by Django 2.2 on 2019-04-09 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50)),
                ('author_phone', models.CharField(max_length=12)),
                ('author_email', models.CharField(max_length=50)),
                ('author_address', models.TextField(max_length=250)),
            ],
        ),
    ]
