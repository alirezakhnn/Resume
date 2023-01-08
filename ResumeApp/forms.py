from django import forms
from .models import ResumeModel

class ResumeForm(forms.ModelForm):
    class Meta:
        model = ResumeModel
        fields = ['pic', 'first_name', 'last_name', 'email', 'history', 'phone_number']
        
        labels = {
            'pic': 'Picture',
            "first_name": "FName",
            "last_name": "LName",
            "email": "Email",
            "history": "History",
            "phone_number": "Phone"
        }
        
        Widgets = {
            'pic': forms.ImageField(),
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'email': forms.CharField(),
            'history': forms.Textarea(),
            'phone_number': forms.IntegerField()
        }
        
        