# Generated by Django 2.2.2 on 2019-06-07 14:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crowdfunder', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='backing',
            name='project',
        ),
        migrations.AddField(
            model_name='backing',
            name='reward',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='backings', to='crowdfunder.Reward'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='backing',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='backings', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reward',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rewards', to='crowdfunder.Project'),
        ),
    ]
