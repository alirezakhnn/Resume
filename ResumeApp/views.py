from django.shortcuts import render
from .models import ResumeModel, ResumeIns
from .forms import ResumeForm, ResumeInsForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(req):
    return render(req, 'ResumeTemp/index.html', {
        "resume": ResumeModel.objects.all(),
        "inss": ResumeIns.objects.all(),
    })

def add(req):
    if req.method == "POST":
        form = ResumeInsForm(req.POST, req.FILES)
        if form.is_valid():
            new_picture_project = form.cleaned_data['picture_project']
            new_name_project = form.cleaned_data['name_project']
            new_summary_project = form.cleaned_data['summary_project']
            
            new_ResumeIns = ResumeIns(
                picture_project = new_picture_project,
                name_project = new_name_project,
                summary_project = new_summary_project
            )
            new_ResumeIns.save()
            return render(req, 'ResumeTemp/add.html', {
                'formIns': ResumeInsForm(),
                'done': True
            })
        else:
            form = ResumeInsForm()
            return render(req, 'ResumeTemp/add.html', {
                'formIns': ResumeInsForm()
            })
    return render(req, 'ResumeTemp/add.html', {
        'formIns': ResumeInsForm()
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
    
    
def delete(req, id):
    if req.method == 'POST':
        resume = ResumeIns.objects.get(pk=id)
        resume.delete()
    return HttpResponseRedirect(reverse('index'))


def editIns(req, id):
    if req.method == 'POST':
        resume = ResumeIns.objects.get(pk=id)
        form = ResumeInsForm(req.POST, req.FILES, instance=resume)
        if form.is_valid():
            form.save()
            return render(req, 'ResumeTemp/edit.html', {
                'form': form,
                'success': True
            })
    else:
        resume = ResumeIns.objects.get(pk=id)
        form = ResumeInsForm(instance=resume)
    return render(req, 'ResumeTemp/edit.html',{
        'form': form
    })