from django.core.exceptions import SynchronousOnlyOperation
from .models import Task
from django import forms


class ModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'priority', 'date']
