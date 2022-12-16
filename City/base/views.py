from django.shortcuts import render
from base.team import Team
def home(request):
    title = 'Home'
    isHospital = False
    return render(request, 'home.html', {'title': title, 'isHospital': isHospital})

def contact(request):
    title = 'Contact Us'
    isHospital = False
    return render(request, 'contact.html', {'title': title, 'isHospital': isHospital})

def about(request):
    title = 'About Us'
    isHospital = False
    teamObj = Team()
    teamData = teamObj.getTeamData()
    key1 = [1,2,3,4,5,6,7,8,9,10]
    key2 = [0,1,2,3,4,5]
    return render(request, 'about.html', {'title': title, 'team': teamData, 'key1': key1, 'key2': key2, 'isHospital': isHospital})