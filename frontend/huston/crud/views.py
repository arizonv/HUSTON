from django.shortcuts import render
import requests
import json


url_api = "http://127.0.0.1:8000/api/developer/"

def getPersona(request):

    response = requests.get(url_api).json()
    datos = {'personas': response}
    return render('home.html', datos)

def gerPrueba(request):

    url_api = "http://127.0.0.1:8000/api/developer/"

    response = requests.get(url_api).json()
    datos = {'persona': response}

    return render(request, 'home.html', datos)
