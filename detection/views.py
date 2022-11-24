from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages


def home(request):
    if request.method == 'POST':
        u=request.POST.get('user')
        e=request.POST.get('email')
        pn=request.POST.get('number')
        p=request.POST.get('password')
        c=request.POST.get('c_password')
        if p==c:
            if User.objects.filter(username=u).exists():
                messages.info(request, 'alre.')
                return render(request, 'index.html')
            else:
                User.objects.create_user(username=u)
                User.objects.create_user(email=e)
                User.objects.create_user(number=pn)
                User.objects.create_user(password=p)
                return render(request, 'index.html')

        else:
            messages.info(request, 'jhjgjhjhbjbnvjvb.')
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')


def log(request):
    pass