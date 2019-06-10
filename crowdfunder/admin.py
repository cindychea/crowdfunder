from django.contrib import admin
from crowdfunder.models import Project, Reward, User, Contribution, Category

admin.site.register(Project)
admin.site.register(Reward)
admin.site.register(User)
admin.site.register(Contribution)
admin.site.register(Category)