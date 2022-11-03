from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model=Project
        # fields='__all__' i merr krejt atributet qe i ka ne models.py->Project
        fields=['title','description','demo_link','source_link','tags']