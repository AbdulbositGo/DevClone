# Generated by Django 4.1.7 on 2023-03-16 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FollowingTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'default_related_name': 'following_tags',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('color', models.CharField(choices=[('DF', 'blue'), ('DK', 'gray'), ('RD', 'red'), ('GR', 'green'), ('YL', 'yellow'), ('ID', 'indigo'), ('PP', 'purple'), ('PK', 'pink')], default='DF', max_length=2)),
            ],
        ),
    ]
