from django.shortcuts import render

def hospital(request):
    title = 'Diagnosing'
    return render(request, 'hospital.html', {'title': title})


#--------------------------------------------------------------------------------------------
#Diagnosing Functionality




#--------------------------------------------------------------------------------------------
def braintumor(request):
    title = 'Brain Tumor'
    return render(request, 'braintumor.html', {'title': title})

def breastcancer(request):
    title = 'Brast Cancer'
    return render(request, 'breastcancer.html', {'title': title})



