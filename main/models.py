from django.db import models

# Create your models here.
class Projects(models.Model):
    name = models.CharField(max_length= 300)
    content = models.TextField(default=None)
    git = models.URLField(max_length=250,default = None)

    class Meta:
        verbose_name_plural = 'Projects'
    def __str__(self):
        return self.name 
    



class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    comments = models.TextField()

    def __str__(self):
        return self.email +' | '+ str(self.comments)