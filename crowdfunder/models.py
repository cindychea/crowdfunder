# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date, datetime
from tagging.fields import TagField


# django.db.utils.IntegrityError:
# The row in table 'crowdfunder_project' with primary key '4'
# has an invalid foreign key: crowdfunder_project.category_id contains a value 'Comics & Illustration'
# that does not have a corresponding value in crowdfunder_category.id.


class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True, null=True)

    def total_contributions(self):
        return sum([c.reward.amount for c in self.contributions.all()])


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    goal = models.IntegerField()
    goal_reached = models.BooleanField(default=False)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    expired = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categories', null=True)
    image = models.ImageField(upload_to='project-image/', null=True, blank=True)
    tags = TagField()

    def __str__(self):
        return self.title

    def total_contributions(self):
        return sum([c.reward.amount for c in self.contributions.all()])

    def project_contributors(self):
        contributors = []
        all_contributions = self.contributions.all()
        for contribution in all_contributions:
            contributors.append(contribution.user.username)
        return set(contributors)

    def active():
        all_projects = Project.objects.all()
        active_projects = []
        for project in all_projects:
            if project.end_date > date.today():
                active_projects.append(project)
        return active_projects

    def expired_project(self):
        if date.today() > self.end_date:
            self.expired = True
            if self.total_contributions() >= self.goal:
                self.goal_reached = True
                return self.goal_reached
        return self.expired

    def countdown(self):
        now = date.today()
        time_left = self.end_date - now
        if time_left.days <= 0:
            return 'None'
        else:
            return time_left.days

    def success():
        all_projects = Project.objects.all()
        projects = []
        for project in all_projects:
            if project.total_contributions() >= project.goal:
                project.goal_reached = True
                projects.append(project)
        return projects

    def unsuccessful():
        all_projects = Project.objects.all()
        projects = []
        for project in all_projects:
            if project.total_contributions() <= project.goal and date.today() > project.end_date:
                projects.append(project)
        return projects

    def funded():
        funded = len(Project.success())
        return funded

    def failed():
        failed = []
        for project in Project.objects.all():
            if project.expired == True and project.goal_reached == False:
                failed.append(project)
        return failed

    def percentage_funded():
        total = len(Project.objects.all())
        percent_funded = Project.funded() / total * 100
        return format(percent_funded, '.0f')

    def percentage_failed():
        total = len(Project.objects.all())
        percent_failed = len(Project.failed()) / total * 100
        return format(percent_failed, '.0f')

    def percentage_in_progress():
        total = len(Project.objects.all())
        percent_ip = (total - Project.funded() - len(Project.failed())) / total * 100
        return format(percent_ip, '.0f')

class Reward(models.Model):
    title = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    limit = models.IntegerField(null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='rewards')

    def __str__(self):
        return f"{self.title} - {self.project}"

    def total_purchased(self):
        total = self.contributions.all().count()
        return total

    def available(self):
        return self.total_purchased() < self.limit or self.limit is None


class Contribution(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contributions')
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE, related_name='contributions')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='contributions')

    def grand_total():
        gt = 0
        for contribution in Contribution.objects.all():
            gt = gt + contribution.reward.amount
        return gt
