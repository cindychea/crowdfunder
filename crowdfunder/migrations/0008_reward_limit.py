# Generated by Django 2.2.1 on 2019-06-10 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdfunder', '0007_project_goal_reached'),
    ]

    operations = [
        migrations.AddField(
            model_name='reward',
            name='limit',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
