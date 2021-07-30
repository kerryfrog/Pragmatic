from django.forms import ModelForm

from projectapp.models import Project


class ProjectCreationForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'image', 'description']   #사용자의 입력으로 받을것
