# Generated by Django 3.1.4 on 2021-01-02 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('home', '0006_auto_20210102_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='blog_listing_section',
            field=models.ForeignKey(blank=True, help_text='First blog listing section for the homepage. Will display up to three child items.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Blog listing section'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='blog_listing_section_title',
            field=models.CharField(blank=True, help_text='Title to display above the blog section copy', max_length=255, null=True),
        ),
    ]
