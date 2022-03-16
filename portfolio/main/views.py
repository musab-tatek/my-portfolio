from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail


def home(request):
    if (request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = 'Contact Form'
        message = request.POST.get('message')
        
        data = {
            'name' : name,
            'email' : email,
            'subject' : subject,
            'message' : message
        }
        message = '''
        Name : {}
        Email : {}
        Message : {}

        '''.format(data['name'], data['email'], data['message'])
        send_mail(data['subject'], message, '', ['musabtatek@gmail.com'])
        print(data)
        return redirect('/')
    return render(request, 'main/index.html')
def hsc(request):
    return render(request, 'main/hsc.html')
def eccs(request):
    return render(request, 'main/eccs.html')
def view_404(request, exception=None):
    return render(request, 'main/404.html')