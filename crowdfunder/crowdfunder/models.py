from django.contrib.auth.models import User
from django.db import models


# Effectively the User model
class Profile(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)


class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    goal = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_projects')
    # total = models.IntegerField()

    def total(self):
        return sum([b.amount for b in self.backing.all()])


class Reward(models.Model):
    reward_description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='backer_rewards')


# Join models -> Captures the relatin between Users and Rewards
class Backing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='backers')
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE, related_name='rewards')
    amount = models.IntegerField()

