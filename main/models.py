from django.db import models


class UsersMessages(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    message = models.TextField()
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "users_messages"
        ordering = ['-created_at']
        verbose_name = "User's Message"
        verbose_name_plural = "User's Messages"