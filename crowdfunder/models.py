# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date, datetime

class User(AbstractUser):
    def total_contributions(self):
        return sum([c.reward.amount for c in self.contributions.all()])


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    goal = models.IntegerField()
    goal_reached = models.BooleanField(default=False)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    expired = models.BooleanField(default=False)
    
    def project_contributors(self):
        contributors = []
        all_contributions = self.contributions.all()
        for contribution in all_contributions:
            contributors.append(contribution.user.username)
        return set(contributors)


    def expired_project(self):
        if date.today() > self.end_date:
            self.expired = True
            if self.total_contributions() >= self.goal:
                self.goal_reached = True
                return self.goal_reached
        return self.expired

    def countdown(self):
        now = date.now()
        time_left = self.end_date - now
        return time_left.days

class Reward(models.Model):
    title = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    limit = models.IntegerField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='rewards')

    def total_purchased(self):
        total = self.contributions.all().count()
        return total


class Contribution(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contributions')
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE, related_name='contributions')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='contributions')

