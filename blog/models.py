from django.db import models
from django.contrib.auth import models as auth_models

# Create your models here.
class BlogUser(models.Model):
    login = models.TextField(max_length = 16)
    password = models.TextField(max_length = 8)

    def __str__(self):
        return f"User {self.login}"

class BlogAuthor(models.Model):
    name = models.TextField(max_length = 16)
    bio = models.TextField(max_length = 256)

    def __str__(self):
        return f"Blog author {self.name} bio '{self.bio}'"

class Blog(models.Model):
    name = models.TextField(max_length=24)
    description = models.TextField(max_length=128)
    post_date = models.DateTimeField(auto_now_add=True)
    author = BlogUser()

    def __str__(self):
        return f"Blog {self.name} about '{self.description}', birthdate {self.post_date}"

class BlogComment(models.Model):
    description = models.TextField(max_length=128)
    post_date = models.DateTimeField(auto_now_add=True)
    ###author = User[1]
    ###blog = Blog[1]

    def __str__(self):
        return f"Blog comment '{self.description}', birthdate {self.post_date}"