from django import forms
from .models import Todo

class TodosForm(forms.ModelForm):
    class Meta : 
        model = Todo
        fields = [
            'task',
            'description',
            'status',
        ]
        widgets = {
            'task' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Task Name...'
                }
            ),
            'description' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Description Task...'
                }
            ),
            'status' : forms.Select(
                attrs={
                    'class' : 'form-control',
                }
            ),
        }