from django.db import models

# Create your models here.
class Project(models.Model):
    name= models.CharField(max_length=200)
    
    # Update Project name on admin
    def __str__(self) -> str:
        return self.name 

class Task(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    project=models.ForeignKey(Project, on_delete=models.CASCADE)

        # Update Project name on admin
    def __str__(self) -> str:
        return self.title 
