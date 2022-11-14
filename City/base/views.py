from django.shortcuts import render

def home(request):
    title = 'Home'
    return render(request, 'home.html', {'title': title})
