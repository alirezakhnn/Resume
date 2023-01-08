from django import forms
from .models import ResumeModel, ResumeIns

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
        
        
        
class ResumeInsForm(forms.ModelForm):
    class Meta:
        model = ResumeIns
        fields = ['picture_project', 'name_project', 'summary_project']
        
        labels = {
            'picture_project': 'projectPoster',
            'name_project': 'projectName',
            'summary_project': 'summary'
        }
        
        Widgets = {
            'picture_project': forms.ImageField(),
            'name_project': forms.TextInput(),
            'summary_project': forms.TextInput()
        }