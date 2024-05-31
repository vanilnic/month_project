from django.shortcuts import render, redirect, reverse

def index(request):
    return render(request, 'pols/index.html')

def offers(request):
    return render(request, 'pols/filter.html')

def favorites(request):
    if request.method == 'GET':
        try:
            print(request.GET['back'])
            return request.META['HTTP_REFERER']
        except:
            print('hui')
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