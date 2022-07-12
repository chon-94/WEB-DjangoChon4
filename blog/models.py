from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse

class User(AbstractUser):
    pass

    def __str__(self):
        return self.username

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title  = models.CharField(max_length=50)
    abstract    = models.TextField()
    thumbnail   = models.ImageField()

    title_1    = models.CharField(blank=True,max_length=50)
    content_1  = models.TextField(blank=True)
    nombreco_1 = models.CharField(blank=True,max_length=50)
    code_1     = models.TextField(blank=True)
    cita_1     = models.CharField(max_length=50,blank=True)

    title_2    = models.CharField(blank=True,max_length=50)
    content_2  = models.TextField(blank=True)
    nombreco_2 = models.CharField(blank=True,max_length=50)
    code_2     = models.TextField(blank=True)
    cita_2     = models.CharField(max_length=50,blank=True)

    title_3    = models.CharField(blank=True,max_length=50)
    content_3  = models.TextField(blank=True)
    nombreco_3 = models.CharField(blank=True,max_length=50)
    code_3     = models.TextField(blank=True)
    cita_3     = models.CharField(max_length=50,blank=True)

    title_4    = models.CharField(blank=True,max_length=50)
    content_4  = models.TextField(blank=True)
    nombreco_4 = models.CharField(blank=True,max_length=50)
    code_4     = models.TextField(blank=True)
    cita_4     = models.CharField(max_length=50,blank=True)

    title_5    = models.CharField(blank=True,max_length=50)
    content_5  = models.TextField(blank=True)
    nombreco_5 = models.CharField(blank=True,max_length=50)
    code_5     = models.TextField(blank=True)
    cita_5     = models.CharField(max_length=50,blank=True)

    publish_date = models.DateField(auto_now_add=True)
    last_updated = models.DateField(auto_now=True)
    
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})

class Script(models.Model):

    dev = models.CharField(max_length=25)
    script = models.FileField()
    Lenguaje = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=75)
    os     = models.CharField(max_length=25)
    
    def __str__(self):
        return self.dev