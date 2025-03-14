from django.shortcuts import render, redirect
from .models import Report, Signalement
from .forms import ReportForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import Report
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html')

def authentification(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email') 
        if username and email:
            user, created = User.objects.get_or_create(
                username=username,
                defaults={"email": email}
            )
            login(request, user)
            return redirect('plainte')
        else:
            messages.error(request, 'Veuillez fournir un nom et une adresse e-mail valides.')
    return render(request, 'authentification.html') 

@login_required
def rapport(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()
            return redirect('detail', report_id=report.id)
    else:
        form = ReportForm()
    return render(request, 'rapport.html', {'form': form})


@login_required
def plainte(request):
    reports = Report.objects.filter(user=request.user)
    return render(request, 'plainte.html', {'reports': reports})

def detail(request, report_id):
    report = get_object_or_404(Report, id=report_id) 
    request.session['signalement_id'] = report.id
    return render(request, 'detail.html', {'report': report})  

def final(request):
    return render(request, 'final.html')

def bientot(request):
    return render(request, 'bientot.html')

from django.urls import reverse

def modifier(request):
    signalement_id = request.session.get('signalement_id')
    if not signalement_id:
        return redirect('modifier')
    signalement = get_object_or_404(Report, id=signalement_id)
    if request.method == 'POST':
        signalement.category = request.POST.get('category')
        signalement.description = request.POST.get('description')
        signalement.location = request.POST.get('Localisation')
        signalement.save()
        return redirect('detail', report_id=signalement.id)
    return render(request, 'modifier.html', {'signalement': signalement})
