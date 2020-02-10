# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# # Create your models here.
# class login_users(models.Model):
#     # user = models.ForeignKey(User)
#     book_id = models.IntegerField()
#     # book_names = models.CharField(max_length=75)
#     # book_publisher = models.CharField(max_length=50)
#     # class Meta:
#     #     db_table = "login_users"
#
# login_users=login_users.objects.Create

class Hero(models.Model):
    name = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)

    def __str__(self):
        return self.name

