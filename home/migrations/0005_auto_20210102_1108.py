# Generated by Django 3.1.4 on 2021-01-02 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210101_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='featuredPost2_author',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='featuredPost2_category',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='featuredPost2_date',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='featuredPost2_discription',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='featuredPost2_title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]