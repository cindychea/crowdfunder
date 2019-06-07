from django.contrib.auth.models import User
from django.db import models
from datetime import date


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    goal = models.IntegerField()
    start_date = models.DateField(default=date.today)
    end_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')

    def total_contributions(self):
        # total = 0
        # for reward_value in self.rewards.all():
        #     total += (reward_value.amount * len(reward_value.backings.all()))
        total = sum([c.reward.amount for c in self.contributions.all()])
        return total
    
    def project_contributors(self):
        contributors = []
        all_contributions = self.contributions.all()
        for contribution in all_contributions:
            contributors.append(contribution.user.username)
        return set(contributors)

class Reward(models.Model):
    title = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='rewards')


class Contribution(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contributions')
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE, related_name='contributions')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='contributions')
