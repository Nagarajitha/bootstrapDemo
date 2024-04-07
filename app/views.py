from django.shortcuts import render

# Create your views here.
def alerts(request):
    return render(request,'alerts.html')

def badges(request):
    return render(request,'badges.html')


def breadcrumb(request):
    return render(request,'breadcrumb.html')

def buttons(request):
    return render(request,'buttons.html')

def buttongroup(request):
    return render(request,'buttongroup.html')

def card(request):
    return render(request,'card.html')

def carousel(request):
    return render(request,'carousel.html')




    



