# Generated by Django 2.1 on 2018-08-27 20:24

import django.contrib.postgres.search
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('tagline', models.TextField()),
                ('lang', models.CharField(default='english', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=255)),
                ('body_text', models.TextField()),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('mod_date', models.DateField(auto_now=True)),
                ('n_comments', models.IntegerField(default=0)),
                ('n_pingbacks', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=5)),
                ('search_vector', django.contrib.postgres.search.SearchVectorField(null=True)),
                ('authors', models.ManyToManyField(to='search_app.Author')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='search_app.Blog')),
            ],
        ),
    ]
