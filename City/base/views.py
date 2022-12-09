from django.shortcuts import render
from base.team import Team
def home(request):
    title = 'Home'
    return render(request, 'home.html', {'title': title})

def contact(request):
    title = 'Contact Us'
    return render(request, 'contact.html', {'title': title})

def about(request):
    title = 'About Us'
    teamObj = Team()
    teamData = teamObj.getTeamData()
    key1 = [1,2,3,4,5,6,7,8,9,10]
    key2 = [0,1,2,3,4,5]
    return render(request, 'about.html', {'title': title, 'team': teamData, 'key1': key1, 'key2': key2})