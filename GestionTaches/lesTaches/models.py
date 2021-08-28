
from django.db import models
from django.contrib import admin
from django.db.models.fields import DateField, DateTimeCheckMixin
from datetime import timedelta,date
from django.utils.html import format_html
# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=250)
    description =  models.TextField()
    created_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(null=True)
    schedule_date = models.DateField(null=True)
    closed = models.BooleanField(default=False)

    def __str__(self):
                 return self.name

    """ @admin.display()
    def clored_due_date(self):
        due_date = date(self.due_date)
        if self.due_date - timedelta(days=7) > date.today():
            color = "green"
        if self.due_date  < date.today():
            color = "red"
        else :
            color = "orange"
        return format_html('<span style= color:%s>%s</span>' %(color,self.due_date))"""
