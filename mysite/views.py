import json

import requests
from django.shortcuts import render

from .models import Contact


def index(request):
    if request.method == 'POST':

        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')

        r = requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName=' + lastname)
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')
        context = {'joke': joke}

        return render(request, 'mysite/index.html', context)

    else:
        r = requests.get('http://api.icndb.com/jokes/random?firstName=Attreya&lastName=Bhatt')
        json_data = json.loads(r.text)
        joke = json_data.get('value').get('joke')
        context = {'joke': joke}
        return render(request, 'mysite/index.html', context)


def portfolio(request):
    return render(request, 'mysite/portfolio.html')


def contact(request):
    if request.method == 'POST':
        email_r = request.POST.get('email')
        subject_r = request.POST.get('subject')
        message_r = request.POST.get('message')

        c = Contact(email=email_r, subject=subject_r, message=message_r)
        c.save()

        return render(request, 'mysite/thank.html')
    else:
        return render(request, 'mysite/contact.html')
