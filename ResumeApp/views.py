from django.shortcuts import render
from .models import ResumeModel
from .forms import ResumeForm

def index(req):
    return render(req, 'ResumeTemp/index.html', {
        "resume": ResumeModel.objects.all()
    })

def edit(req, id):
    if req.method == 'POST':
        resume = ResumeModel.objects.get(pk=id)
        form = ResumeForm(req.POST, req.FILES, instance=resume)
        if form.is_valid():
            form.save()
            return render(req, 'ResumeTemp/edit.html', {
                'form': form,
                'success': True
            })
    else:
        resume = ResumeModel.objects.get(pk=id)
        form = ResumeForm(instance=resume)
    return render(req, 'ResumeTemp/edit.html',{
        'form': form
    })
