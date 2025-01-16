# Generated by Django 5.1.4 on 2025-01-15 18:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_blog_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='published',
            field=models.DateTimeField(db_default=datetime.datetime(2025, 1, 16, 7, 0, tzinfo=datetime.timezone.utc), help_text='The publish time of the project'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='published',
            field=models.DateTimeField(db_default=datetime.datetime(2025, 1, 16, 7, 0, tzinfo=datetime.timezone.utc), help_text='The publish time of the blog'),
        ),
    ]
