# Generated by Django 3.1.3 on 2020-11-27 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0002_auto_20201123_0402'),
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_text', models.CharField(max_length=120)),
            ],
        ),
    ]
