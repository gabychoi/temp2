# Generated by Django 2.2.5 on 2020-12-02 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filterApp', '0005_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]