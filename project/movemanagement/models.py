from django.db import models



class ProjectUser(models.Model):
    username=models.CharField(max_length=50, unique=True)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.username

   
class Documentation(models.Model):
    projectname=models.CharField(max_length=50)
    description=models.TextField(null=True, blank=True)
    # image=models.ImageField(upload_to='images/')
    documentation=models.FileField(upload_to='documentations/')

    def __str__(self):
        return self.projectname

class Project(models.Model):
    image=models.ImageField(upload_to='images/',null=True,blank=True)
    Projectname=models.CharField(max_length=50)
    date=models.DateField(auto_now_add=True) 
    url=models.URLField(max_length=50)
    projectuser=models.ManyToManyField(ProjectUser)
    documentation=models.ManyToManyField(Documentation)
    # users=models.ForeignKey('auth.user',on_delete=models.PROTECT,null=True,blank=True)
   

    def __str__(self):
        return f"{self.Projectname}, {self.url}"
