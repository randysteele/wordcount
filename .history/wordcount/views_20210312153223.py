from django.http import HttpResponse 
from django.shortcuts import render 

def homepage(request):
    return render(request, 'home.html')
    

def count(request):
    fulltext = request.ET['fulltext']
    return render (request, 'count.html')    


    

    
