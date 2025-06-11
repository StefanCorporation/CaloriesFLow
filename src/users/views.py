from django.shortcuts import render
from django.contrib import auth
from django.urls import reverse
from django.http import HttpResponseRedirect


from users.forms import UserLoginForm, UserRegistrationForm



def login(request):

    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)

        print(request.POST)
        print(form.error_messages)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)

            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('home:index'))
        
    else:
        form = UserLoginForm()


    context = {
        'title': 'Home',
        'form': form,
    }


    return render(request, 'login.html', context=context)



def registration(request):

    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)

        print(request.POST)
        print(form.error_messages)

        if form.is_valid():
            form.save()

            user = form.instance
            auth.login(request, user)

            return HttpResponseRedirect(reverse('home:index'))       
    else:
        form = UserRegistrationForm()

    context = {
        'title': 'Registration',
        'form': form,
    }

    return render(request, 'registration.html', context=context)


def profile(request):
    return render(request, 'profile.html')