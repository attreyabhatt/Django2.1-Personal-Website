from django.shortcuts import render

from .models import Contact


def index(request):
    return render(request, 'mysite/index.html')


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
