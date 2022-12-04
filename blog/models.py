from django.db import models
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse

class User(AbstractUser):
    pass

    def __str__(self):
        return self.username

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title  = models.CharField(max_length=100)
    abstract    = models.TextField()
    thumbnail   = models.ImageField()

    title_1    = models.CharField(blank=True,max_length=175)
    content_1  = models.TextField(blank=True)
    
    subtitle_1_1_1 = models.CharField(blank=True,max_length=175)
    subcontet_1_1_1 = models.TextField(blank=True)
    code_1_1_1 = models.TextField(blank=True)
    puntotitle_1_1_1 = models.CharField(blank=True,max_length=175)
    puntocontet_1_1_1 = models.TextField(blank=True)
    puntotitle_1_2_1 = models.CharField(blank=True,max_length=175)
    puntocontet_1_2_1 = models.TextField(blank=True)
    
    subtitle_1_1_2 = models.CharField(blank=True,max_length=175)
    subcontet_1_1_2 = models.TextField(blank=True)
    code_1_1_2 = models.TextField(blank=True)
    puntotitle_1_1_2 = models.CharField(blank=True,max_length=175)
    puntocontet_1_1_2 = models.TextField(blank=True)
    puntotitle_1_2_2 = models.CharField(blank=True,max_length=175)
    puntocontet_1_2_2 = models.TextField(blank=True)
    
    subtitle_1_1_3 = models.CharField(blank=True,max_length=175)
    subcontet_1_1_3 = models.TextField(blank=True)
    code_1_1_3 = models.TextField(blank=True)
    puntotitle_1_1_3 = models.CharField(blank=True,max_length=175)
    puntocontet_1_1_3 = models.TextField(blank=True)
    puntotitle_1_2_3 = models.CharField(blank=True,max_length=175)
    puntocontet_1_2_3 = models.TextField(blank=True)
    
    subtitle_1_1_4 = models.CharField(blank=True,max_length=175)
    subcontet_1_1_4 = models.TextField(blank=True)
    code_1_1_4 = models.TextField(blank=True)
    puntotitle_1_1_4 = models.CharField(blank=True,max_length=175)
    puntocontet_1_1_4 = models.TextField(blank=True)
    puntotitle_1_2_4 = models.CharField(blank=True,max_length=175)
    puntocontet_1_2_4 = models.TextField(blank=True)
    
    subtitle_1_1_5 = models.CharField(blank=True,max_length=175)
    subcontet_1_1_5 = models.TextField(blank=True)
    code_1_1_5 = models.TextField(blank=True)
    puntotitle_1_1_5 = models.CharField(blank=True,max_length=175)
    puntocontet_1_1_5 = models.TextField(blank=True)
    puntotitle_1_2_5 = models.CharField(blank=True,max_length=175)
    puntocontet_1_2_5 = models.TextField(blank=True)    
    
    nombreco_1 = models.CharField(blank=True,max_length=200)
    code_1     = models.TextField(blank=True)
    cita_1_0     = models.CharField(max_length=750,blank=True)
    cita_1_1     = models.CharField(max_length=750,blank=True)
    cita_1_2     = models.CharField(max_length=750,blank=True)
    cita_1_3     = models.CharField(max_length=750,blank=True)
    cita_1_4     = models.CharField(max_length=750,blank=True)

    title_2    = models.CharField(blank=True,max_length=175)
    content_2  = models.TextField(blank=True)
    
    subtitle_2_1_1 = models.CharField(blank=True,max_length=175)
    subcontet_2_1_1 = models.TextField(blank=True)
    code_2_1_1 = models.TextField(blank=True)
    puntotitle_2_1_1 = models.CharField(blank=True,max_length=175)
    puntocontet_2_1_1 = models.TextField(blank=True)
    puntotitle_2_2_1 = models.CharField(blank=True,max_length=175)
    puntocontet_2_2_1 = models.TextField(blank=True)
    
    subtitle_2_1_2 = models.CharField(blank=True,max_length=175)
    subcontet_2_1_2 = models.TextField(blank=True)
    code_2_1_2 = models.TextField(blank=True)
    puntotitle_2_1_2 = models.CharField(blank=True,max_length=175)
    puntocontet_2_1_2 = models.TextField(blank=True)
    puntotitle_2_2_2 = models.CharField(blank=True,max_length=175)
    puntocontet_2_2_2 = models.TextField(blank=True)
    
    subtitle_2_1_3 = models.CharField(blank=True,max_length=175)
    subcontet_2_1_3 = models.TextField(blank=True)
    code_2_1_3 = models.TextField(blank=True)
    puntotitle_2_1_3 = models.CharField(blank=True,max_length=175)
    puntocontet_2_1_3 = models.TextField(blank=True)
    puntotitle_2_2_3 = models.CharField(blank=True,max_length=175)
    puntocontet_2_2_3 = models.TextField(blank=True)
    
    subtitle_2_1_4 = models.CharField(blank=True,max_length=175)
    subcontet_2_1_4 = models.TextField(blank=True)
    code_2_1_4 = models.TextField(blank=True)
    puntotitle_2_1_4 = models.CharField(blank=True,max_length=175)
    puntocontet_2_1_4 = models.TextField(blank=True)
    puntotitle_2_2_4 = models.CharField(blank=True,max_length=175)
    puntocontet_2_2_4 = models.TextField(blank=True)
    
    subtitle_2_1_5 = models.CharField(blank=True,max_length=175)
    subcontet_2_1_5 = models.TextField(blank=True)
    code_2_1_5 = models.TextField(blank=True)
    puntotitle_2_1_5 = models.CharField(blank=True,max_length=175)
    puntocontet_2_1_5 = models.TextField(blank=True)
    puntotitle_2_2_5 = models.CharField(blank=True,max_length=175)
    puntocontet_2_2_5 = models.TextField(blank=True)    
    
    nombreco_2 = models.CharField(blank=True,max_length=200)
    code_2     = models.TextField(blank=True)
    cita_2_0     = models.CharField(max_length=750,blank=True)
    cita_2_1     = models.CharField(max_length=750,blank=True)
    cita_2_2     = models.CharField(max_length=750,blank=True)
    cita_2_3     = models.CharField(max_length=750,blank=True)
    cita_2_4     = models.CharField(max_length=750,blank=True)

    title_3    = models.CharField(blank=True,max_length=175)
    content_3  = models.TextField(blank=True)
    
    subtitle_3_1_1 = models.CharField(blank=True,max_length=175)
    subcontet_3_1_1 = models.TextField(blank=True)
    code_3_1_1 = models.TextField(blank=True)
    puntotitle_3_1_1 = models.CharField(blank=True,max_length=175)
    puntocontet_3_1_1 = models.TextField(blank=True)
    puntotitle_3_2_1 = models.CharField(blank=True,max_length=175)
    puntocontet_3_2_1 = models.TextField(blank=True)
    
    subtitle_3_1_2 = models.CharField(blank=True,max_length=175)
    subcontet_3_1_2 = models.TextField(blank=True)
    code_3_1_2 = models.TextField(blank=True)
    puntotitle_3_1_2 = models.CharField(blank=True,max_length=175)
    puntocontet_3_1_2 = models.TextField(blank=True)
    puntotitle_3_2_2 = models.CharField(blank=True,max_length=175)
    puntocontet_3_2_2 = models.TextField(blank=True)
    
    subtitle_3_1_3 = models.CharField(blank=True,max_length=175)
    subcontet_3_1_3 = models.TextField(blank=True)
    code_3_1_3 = models.TextField(blank=True)
    puntotitle_3_1_3 = models.CharField(blank=True,max_length=175)
    puntocontet_3_1_3 = models.TextField(blank=True)
    puntotitle_3_2_3 = models.CharField(blank=True,max_length=175)
    puntocontet_3_2_3 = models.TextField(blank=True)
    
    subtitle_3_1_4 = models.CharField(blank=True,max_length=175)
    subcontet_3_1_4 = models.TextField(blank=True)
    code_3_1_4 = models.TextField(blank=True)
    puntotitle_3_1_4 = models.CharField(blank=True,max_length=175)
    puntocontet_3_1_4 = models.TextField(blank=True)
    puntotitle_3_2_4 = models.CharField(blank=True,max_length=175)
    puntocontet_3_2_4 = models.TextField(blank=True)
    
    subtitle_3_1_5 = models.CharField(blank=True,max_length=175)
    subcontet_3_1_5 = models.TextField(blank=True)
    code_3_1_5 = models.TextField(blank=True)
    puntotitle_3_1_5 = models.CharField(blank=True,max_length=175)
    puntocontet_3_1_5 = models.TextField(blank=True)
    puntotitle_3_2_5 = models.CharField(blank=True,max_length=175)
    puntocontet_3_2_5 = models.TextField(blank=True)    
    
    nombreco_3 = models.CharField(blank=True,max_length=200)
    code_3     = models.TextField(blank=True)
    cita_3_0     = models.CharField(max_length=750,blank=True)
    cita_3_1     = models.CharField(max_length=750,blank=True)
    cita_3_2     = models.CharField(max_length=750,blank=True)
    cita_3_3     = models.CharField(max_length=750,blank=True)
    cita_3_4     = models.CharField(max_length=750,blank=True)

    title_4    = models.CharField(blank=True,max_length=175)
    content_4  = models.TextField(blank=True)
    
    subtitle_4_1_1 = models.CharField(blank=True,max_length=175)
    subcontet_4_1_1 = models.TextField(blank=True)
    code_4_1_1 = models.TextField(blank=True)
    puntotitle_4_1_1 = models.CharField(blank=True,max_length=175)
    puntocontet_4_1_1 = models.TextField(blank=True)
    puntotitle_4_2_1 = models.CharField(blank=True,max_length=175)
    puntocontet_4_2_1 = models.TextField(blank=True)
    
    subtitle_4_1_2 = models.CharField(blank=True,max_length=175)
    subcontet_4_1_2 = models.TextField(blank=True)
    code_4_1_2 = models.TextField(blank=True)
    puntotitle_4_1_2 = models.CharField(blank=True,max_length=175)
    puntocontet_4_1_2 = models.TextField(blank=True)
    puntotitle_4_2_2 = models.CharField(blank=True,max_length=175)
    puntocontet_4_2_2 = models.TextField(blank=True)
    
    subtitle_4_1_3 = models.CharField(blank=True,max_length=175)
    subcontet_4_1_3 = models.TextField(blank=True)
    code_4_1_3 = models.TextField(blank=True)
    puntotitle_4_1_3 = models.CharField(blank=True,max_length=175)
    puntocontet_4_1_3 = models.TextField(blank=True)
    puntotitle_4_2_3 = models.CharField(blank=True,max_length=175)
    puntocontet_4_2_3 = models.TextField(blank=True)
    
    subtitle_4_1_4 = models.CharField(blank=True,max_length=175)
    subcontet_4_1_4 = models.TextField(blank=True)
    code_4_1_4 = models.TextField(blank=True)
    puntotitle_4_1_4 = models.CharField(blank=True,max_length=175)
    puntocontet_4_1_4 = models.TextField(blank=True)
    puntotitle_4_2_4 = models.CharField(blank=True,max_length=175)
    puntocontet_4_2_4 = models.TextField(blank=True)
    
    subtitle_4_1_5 = models.CharField(blank=True,max_length=175)
    subcontet_4_1_5 = models.TextField(blank=True)
    code_4_1_5 = models.TextField(blank=True)
    puntotitle_4_1_5 = models.CharField(blank=True,max_length=175)
    puntocontet_4_1_5 = models.TextField(blank=True)
    puntotitle_4_2_5 = models.CharField(blank=True,max_length=175)
    puntocontet_4_2_5 = models.TextField(blank=True)    
    
    nombreco_4 = models.CharField(blank=True,max_length=200)
    code_4     = models.TextField(blank=True)
    cita_4_0     = models.CharField(max_length=750,blank=True)
    cita_4_1     = models.CharField(max_length=750,blank=True)
    cita_4_2     = models.CharField(max_length=750,blank=True)
    cita_4_3     = models.CharField(max_length=750,blank=True)
    cita_4_4     = models.CharField(max_length=750,blank=True)

    title_5    = models.CharField(blank=True,max_length=175)
    content_5  = models.TextField(blank=True)
    
    subtitle_5_1_1 = models.CharField(blank=True,max_length=175)
    subcontet_5_1_1 = models.TextField(blank=True)
    code_5_1_1 = models.TextField(blank=True)
    puntotitle_5_1_1 = models.CharField(blank=True,max_length=175)
    puntocontet_5_1_1 = models.TextField(blank=True)
    puntotitle_5_2_1 = models.CharField(blank=True,max_length=175)
    puntocontet_5_2_1 = models.TextField(blank=True)
    
    subtitle_5_1_2 = models.CharField(blank=True,max_length=175)
    subcontet_5_1_2 = models.TextField(blank=True)
    code_5_1_2 = models.TextField(blank=True)
    puntotitle_5_1_2 = models.CharField(blank=True,max_length=175)
    puntocontet_5_1_2 = models.TextField(blank=True)
    puntotitle_5_2_2 = models.CharField(blank=True,max_length=175)
    puntocontet_5_2_2 = models.TextField(blank=True)
    
    subtitle_5_1_3 = models.CharField(blank=True,max_length=175)
    subcontet_5_1_3 = models.TextField(blank=True)
    code_5_1_3 = models.TextField(blank=True)
    puntotitle_5_1_3 = models.CharField(blank=True,max_length=175)
    puntocontet_5_1_3 = models.TextField(blank=True)
    puntotitle_5_2_3 = models.CharField(blank=True,max_length=175)
    puntocontet_5_2_3 = models.TextField(blank=True)
    
    subtitle_5_1_4 = models.CharField(blank=True,max_length=175)
    subcontet_5_1_4 = models.TextField(blank=True)
    code_5_1_4 = models.TextField(blank=True)
    puntotitle_5_1_4 = models.CharField(blank=True,max_length=175)
    puntocontet_5_1_4 = models.TextField(blank=True)
    puntotitle_5_2_4 = models.CharField(blank=True,max_length=175)
    puntocontet_5_2_4 = models.TextField(blank=True)
    
    subtitle_5_1_5 = models.CharField(blank=True,max_length=175)
    subcontet_5_1_5 = models.TextField(blank=True)
    code_5_1_5 = models.TextField(blank=True)
    puntotitle_5_1_5 = models.CharField(blank=True,max_length=175)
    puntocontet_5_1_5 = models.TextField(blank=True)
    puntotitle_5_2_5 = models.CharField(blank=True,max_length=175)
    puntocontet_5_2_5 = models.TextField(blank=True)    
    
    nombreco_5 = models.CharField(blank=True,max_length=200)
    code_5     = models.TextField(blank=True)
    cita_5_0     = models.CharField(max_length=750,blank=True)
    cita_5_1     = models.CharField(max_length=750,blank=True)
    cita_5_2     = models.CharField(max_length=750,blank=True)
    cita_5_3     = models.CharField(max_length=750,blank=True)
    cita_5_4     = models.CharField(max_length=750,blank=True)
    
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