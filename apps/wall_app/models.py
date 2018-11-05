from __future__ import unicode_literals
from django.db import models
from apps.login_registration.models import User
from datetime import date

class Message(models.Model):
    message = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name='user_message', on_delete = models.CASCADE)

class Comment(models.Model):
    comment = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment_msg = models.ForeignKey(Message, related_name='message_comment', on_delete = models.CASCADE)
    user_msg = models.ForeignKey(User, related_name='user_comment', on_delete = models.CASCADE)

def is_past_due(self):
    return date.today() > self.date
