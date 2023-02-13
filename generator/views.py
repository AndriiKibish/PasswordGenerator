from django.shortcuts import render
import random


def about(request):
    return render(request, 'generator/about.html')


def settings(request):
    return render(request, 'generator/settings.html')


def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')

    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):
        characters.extend(list('abcdefghijklmnopqrstuvwxyz'.upper()))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()?'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))

    thepassword = ''

    for i in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})
                  
