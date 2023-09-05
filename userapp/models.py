from django.db import models
from datetime import datetime

# Create your models here.
class Userdb(models.Model):
    Name=models.CharField(max_length=50,null=True,blank=True)
    Username=models.CharField(max_length=50,null=True,blank=True)
    Password=models.CharField(max_length=50,null=True,blank=True)
    Gender=models.CharField(max_length=50,null=True,blank=True)
    Email=models.EmailField(max_length=50,null=True,blank=True)
    Profile=models.ImageField(upload_to='profile',null=True,blank=True)
    Cover=models.ImageField(upload_to='profile',null=True,blank=True)

    def __str__(self):
        return self.Username

class postsdb(models.Model):
    Username=models.ForeignKey(Userdb,null=True,on_delete=models.CASCADE)
    Posts=models.ImageField(upload_to='posts',null=True,blank=True)
    Caption=models.CharField(max_length=200,null=True,blank=True)
    no_of_like=models.IntegerField(default=0)
    post_date=models.DateField(default=datetime.now)
    l_status=models.ManyToManyField(Userdb, related_name='liked_posts', blank=True)


    def __str__(self):
        return self.Username

    def like_post(self, user):
        self.l_status.add(user)

    def remove_like(self, user):
        self.l_status.remove(user)


class followersdb(models.Model):
    Follower=models.ForeignKey(Userdb,null=True,on_delete=models.CASCADE)
    Username=models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.Follower

class likes(models.Model):
    Username=models.CharField(max_length=50,null=True,blank=True)
    post=models.CharField(max_length=50,null=True,blank=True)

class commentdb(models.Model):
    post=models.ForeignKey(postsdb,null=True,on_delete=models.CASCADE)
    User=models.ForeignKey(Userdb,null=True,on_delete=models.CASCADE)
    comment=models.CharField(max_length=500,null=True,blank=True)
    date = models.DateField(default=datetime.now)



