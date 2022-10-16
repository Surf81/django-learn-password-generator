from django.shortcuts import render
from django.http import HttpResponse
import random, string

# Create your views here.
def home(request):
    return render(request, r'generator\home.html')

def password(request):

    characters = list(string.ascii_lowercase)

    if request.GET.get('uppercase', False):
        characters.extend(string.ascii_uppercase)
    if request.GET.get('specials', False):
        characters.extend('!@#$%^&()')
    if request.GET.get('numbers', False):
        characters.extend(string.digits)

    length = int(request.GET.get('length', 12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, r'generator\password.html', {'password': thepassword})

def about(request):
    return render(request, 'generator/about.html')
