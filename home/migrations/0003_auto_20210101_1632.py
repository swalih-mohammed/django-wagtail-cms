# Generated by Django 3.1.4 on 2021-01-01 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='coverstory_discription',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='coverstory_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]