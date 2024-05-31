from django.shortcuts import render, redirect, reverse

def index(request):
    return render(request, 'pols/index.html')

def offers(request):
    return render(request, 'pols/filter.html')

def favorites(request):
    if request.method == 'GET':
        return reverse('')
    return render(request, 'pols/favorites.html')

def travel_history(request):
    return render(request, 'pols/history.html')

