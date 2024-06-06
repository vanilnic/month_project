from django.contrib.auth import get_user_model, authenticate, login
from django.shortcuts import render, redirect, reverse
from django.views.generic import DetailView
from datetime import datetime, timedelta
from .forms import SignUpForm, SignInForm
from .models import *
from django import forms

def index(request, title='/'):
    arrival = datetime.now().strftime("%Y-%m-%d")
    departure = (datetime.now() + timedelta(1)).strftime("%Y-%m-%d")
    people = '1 взрослый'
    supet_title = '/'
    log_in_people = 3
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'pols/index.html', {'log_in_people': log_in_people, 'arrival': arrival, 'departure': departure, 'people': people})
        else:
            return render(request, 'pols/index.html',{'arrival': arrival, 'departure': departure, 'people': people})

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
        elif 'search' in request.POST:
            print('123')
            redirect('offers')

    else:
        return render(request, 'pols/index.html', {'arrival': arrival, 'departure': departure, 'people': people})

def offers(request, city, arrival, departure, people):
    rooms = Rooms.objects.all()
    log_in_people = 3
    print(city)
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'pols/filter.html', {'log_in_people': log_in_people, 'rooms': rooms, 'city':city, 'arrival':arrival, 'departure':departure, 'people':people})
        else:
            return render(request, 'pols/filter.html', {'rooms': rooms})

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
                    return render(request,'pols/filter.html', {'log_in_people': log_in_people, 'rooms': rooms})
                    # return redirect('index')
            else:
                return redirect('offers')


    else:
        return render(request, 'pols/filter.html')

def favorites(request, title=None):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'pols/favorites.html', {'title': title})
        return redirect(request.META.get('HTTP_REFERER'))

    return render(request, 'pols/favorites.html', {'title': title})

def travel_history(request, title=None):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'pols/history.html', {'title': title})
        return redirect(request.META.get('HTTP_REFERER'))

    return render(request, 'pols/history.html', {'title': title})


class PostDetailView(DetailView):
    model = Hotel
    context_object_name = 'object'
    fields = '__all__'
    template_name = 'pols/hotel.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['hotels']=[self.get_object()]
        return context

    def get_object(self, queryset=None):
        return Hotel.objects.get(id=self.kwargs['id_hotel_id'])

def hotel(request, id_hotel_id=None):
    hotels = Hotel.objects.all().filter(id=id_hotel_id)
    rooms = Rooms.objects.all().filter(hotel=id_hotel_id)
    print(hotels)
    # print(Rooms.objects.all()
    log_in_people = 3
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request, 'pols/hotel.html', {'log_in_people': log_in_people, 'hotels': hotels, 'id_hotel_id': id_hotel_id, 'rooms': rooms})
        else:
            return render(request, 'pols/hotel.html', {'hotels': hotels, 'id_hotel_id': id_hotel_id, 'rooms': rooms})

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
            return redirect('hotel_id')

        elif 'login' in request.POST:
            user_form = SignInForm(data=request.POST)
            if user_form.is_valid:
                print('lol')
                user = authenticate(email=request.POST.get('email_aut'), password=request.POST.get('password_aut'))
                if user is not None:
                    login(request,user)
                    return render(request,'pols/hotel.html', {'log_in_people': log_in_people, 'hotels': hotels, 'id_hotel_id': id_hotel_id, 'rooms': rooms})
                    # return redirect('index')
            else:
                return redirect('hotel_id')
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