from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    #good practice to have __str__, because it shows up as object in admin
    def __str__(self):
        return self.title


