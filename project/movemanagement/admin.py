from django.contrib import admin
from .models import Project,ProjectUser,Documentation

# admin.site.register(Project)
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display =  ("Projectname","image","date", "url")
    search_fields = ('projectname','date','url')

@admin.register(ProjectUser)
class ProjectUserAdmin(admin.ModelAdmin):
    list_display = ("username","password")
    search_fields = ('username','password')

@admin.register(Documentation)
class Documentation(admin.ModelAdmin):
    list_display = ("projectname","description","documentation")
    search_fields = ('projectname','description','documentation')



