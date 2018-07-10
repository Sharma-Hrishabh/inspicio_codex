# Generated by Django 2.0.7 on 2018-07-10 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('isbn', models.IntegerField()),
                ('year', models.IntegerField()),
                ('author', models.CharField(max_length=100)),
            ],
        ),
    ]