from django.db import models

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10,blank =True)
    
    def __str__(self):
        return self.first_name
    
    def save_editor(self):
        self.save()
    
    class Meta:
        ordering = ['first_name']
        verbose_name = 'Editor'
        verbose_name_plural = 'Editors'
    
class tags(models.Model):
    name = models.CharField(max_length= 20)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

class Location(models.Model):
    name = models.CharField(max_length= 20)
    
    def save_location(self):
        self.save()
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length= 20)
    
    def save_category(self):
        self.save()
    
    def __str__(self):
        return self.name