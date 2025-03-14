from django.shortcuts import render, redirect
from .models import Report
from .forms import ReportForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import Report

def home(request):
    """ Vue pour la page d'accueil. """
    return render(request, 'home.html')

def authentification(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('plainte') 
        else:
            messages.error(request, 'Identifiants invalides. Veuillez réessayer.')
    return render(request, 'authentification.html') 

def connexion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('plainte') 
        else:
            messages.error(request, 'Identifiants invalides. Veuillez réessayer.')
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
    """ Vue pour afficher le tableau de bord. """
    reports = Report.objects.filter(user=request.user)
    return render(request, 'plainte.html', {'reports': reports})

def detail(request, report_id):
    report = get_object_or_404(Report, id=report_id)
    return render(request, 'detail.html', {'report': report})

def final(request):
    return render(request, 'final.html')

def bientot(request):
    return render(request, 'bientot.html')

from django.urls import reverse

def modifier(request):
    return render(request, 'modifier.html')
