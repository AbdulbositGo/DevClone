# Generated by Django 4.1.4 on 2023-02-06 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
