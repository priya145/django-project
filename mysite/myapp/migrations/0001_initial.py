# Generated by Django 3.0.5 on 2020-09-24 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('asset', models.IntegerField()),
                ('liability', models.IntegerField()),
            ],
        ),
    ]
