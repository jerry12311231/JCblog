from django.shortcuts import render
import datetime

from django.http import HttpResponse



def main(request):
     '''
     Render the main page
     '''
     now = datetime.datetime.now()
     context = {'like':'Django 很棒','now':now}
     return render(request, 'main/main.html', context)
 
def about(request):
     '''
     Render the main page
     '''
     return render(request, 'main/about.html')
 
def contact(request):
     '''
     Render the main page
     '''
     return render(request, 'main/contact.html')
 
 