from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    goal = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')

    def total_fund(self):
        total = 0
        for reward_value in self.reward.all():
            total += (reward_value.amount * len(reward_value.backings.all()))
        return total


class Reward(models.Model):
    title = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='rewards')


class Backing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='backings')
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE, related_name='backings')