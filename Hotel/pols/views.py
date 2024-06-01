from django.contrib.auth import get_user_model, authenticate, login
from django.shortcuts import render, redirect, reverse
from .forms import SignUpForm, SignInForm
from django import forms

def index(request):
    return render(request, 'pols/index.html')

def offers(request):
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
            return redirect('index')
        # else:
        #     return render(request, 'pols/filter.html')

        elif 'login' in request.POST:
            user_form = SignInForm(data=request.POST)
            if user_form.is_valid:
                print('lol')
                user = authenticate(email=request.POST.get('email_aut'), password=request.POST.get('password_aut'))
                if user is not None:
                    login(request,user)
                    return redirect('index')
    else:
        return render(request, 'pols/filter.html')

def favorites(request):
    return render(request, 'pols/favorites.html')

def travel_history(request):
    return render(request, 'pols/history.html')

def hotel(request):
    return render(request, 'pols/hotel.html')

def order(request):
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