from django.contrib.auth import get_user_model, authenticate, login
from django.shortcuts import render, redirect, reverse
from .forms import SignUpForm, SignInForm
from django import forms

def index(request, title='/'):
    supet_title = '/'
    log_in_people = 3
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'pols/index.html', {'log_in_people': log_in_people})

    if request.method == 'POST':
        if 'register' in request.POST:
            user_form = SignUpForm
            if user_form.is_valid:
                email = request.POST.get('email')
                password = request.POST.get('password')
                password2 = request.POST.get('password2')

                if password == password2:
                    User = get_user_model()
                    user = User.objects.create_user(email=email, password=password)
                # profile = Profile.objects.create(user=user, email=email)
                else:
                    return redirect('index')
            return redirect('index')
        # else:
        #     return render(request, 'pols/filter.html')

        elif 'login' in request.POST:
            user_form = SignInForm(data=request.POST)
            if user_form.is_valid:
                print('lol')
                user = authenticate(email=request.POST.get('email_aut'), password=request.POST.get('password_aut'))
                if user is not None:
                    login(request, user)
                    return render(request, 'pols/index.html', {'log_in_people': log_in_people, 'supet_title': supet_title, 'title': title})
                    # return redirect('index')

    else:
        return render(request, 'pols/index.html')

def offers(request):
    log_in_people = 3
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'pols/filter.html', {'log_in_people': log_in_people})

    if request.method == 'POST':
        if 'register' in request.POST:
            user_form = SignUpForm
            if user_form.is_valid:
                email = request.POST.get('email')
                password = request.POST.get('password')
                password2 = request.POST.get('password2')

                if password == password2:
                    User = get_user_model()
                    user = User.objects.create_user(email=email, password=password)
                # profile = Profile.objects.create(user=user, email=email)
                else:
                    return redirect('offers')
            return redirect('offers')
        # else:
        #     return render(request, 'pols/filter.html')

        elif 'login' in request.POST:
            user_form = SignInForm(data=request.POST)
            if user_form.is_valid:
                print('lol')
                user = authenticate(email=request.POST.get('email_aut'), password=request.POST.get('password_aut'))
                if user is not None:
                    login(request,user)
                    return render(request,'pols/filter.html', {'log_in_people': log_in_people})
                    # return redirect('index')
            else:
                return redirect('offers')


    else:
        return render(request, 'pols/filter.html')

def favorites(request, title=None):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'pols/favorites.html', {'title': title})

    return render(request, 'pols/favorites.html', {'title': title})

def travel_history(request, title=None):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'pols/history.html', {'title': title})

    return render(request, 'pols/history.html', {'title': title})

def hotel(request):
    log_in_people = 3
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'pols/hotel.html', {'log_in_people': log_in_people})

    if request.method == 'POST':
        if 'register' in request.POST:
            user_form = SignUpForm
            if user_form.is_valid:
                email = request.POST.get('email')
                password = request.POST.get('password')
                password2 = request.POST.get('password2')

                if password == password2:
                    User = get_user_model()
                    user = User.objects.create_user(email=email, password=password)
                # profile = Profile.objects.create(user=user, email=email)
                else:
                    return redirect('hotel')
            return redirect('hotel')

        elif 'login' in request.POST:
            user_form = SignInForm(data=request.POST)
            if user_form.is_valid:
                print('lol')
                user = authenticate(email=request.POST.get('email_aut'), password=request.POST.get('password_aut'))
                if user is not None:
                    login(request,user)
                    return render(request,'pols/hotel.html', {'log_in_people': log_in_people})
                    # return redirect('index')
            else:
                return redirect('hotel')
    else:
        return render(request, 'pols/hotel.html')

def order(request):
    log_in_people = 3
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'pols/making_an_order.html', {'log_in_people': log_in_people})

    if request.method == 'POST':
        if 'register' in request.POST:
            user_form = SignUpForm
            if user_form.is_valid:
                email = request.POST.get('email')
                password = request.POST.get('password')
                password2 = request.POST.get('password2')

                if password == password2:
                    User = get_user_model()
                    user = User.objects.create_user(email=email, password=password)
                # profile = Profile.objects.create(user=user, email=email)
                else:
                    return redirect('order')
            return redirect('order')
        # else:
        #     return render(request, 'pols/filter.html')

        elif 'login' in request.POST:
            user_form = SignInForm(data=request.POST)
            if user_form.is_valid:
                print('lol')
                user = authenticate(email=request.POST.get('email_aut'), password=request.POST.get('password_aut'))
                if user is not None:
                    login(request, user)
                    return render(request, 'pols/making_an_order.html', {'log_in_people': log_in_people})
                    # return redirect('index')
            else:
                return redirect('order')
    else:
        return render(request, 'pols/making_an_order.html')

def payments(request):
    return render(request, 'pols/payments.html')

def successful_payment(request):
    return render(request, 'pols/successfully.html')

# def registrarion(request):
    # if request.method == 'POST':
    #     user_form = SignUpForm
    #     if user_form.is_valid():
    #         user_form.save()
    #     return redirect('index')