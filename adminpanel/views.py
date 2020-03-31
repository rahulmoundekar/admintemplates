from django.shortcuts import render
import logging

def dashboard(request):
    logging.info('request hit to dashboard')
    return render(request, 'index.html')


def aboutUs(request):
    return render(request, 'about.html')


def contactUs(request):
    return render(request, 'contact.html')


def employees(request):
    return render(request, 'form.html')
