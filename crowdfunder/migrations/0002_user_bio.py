# Generated by Django 2.2.1 on 2019-06-10 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdfunder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]