from django.shortcuts import render

# Create your views here.
def firstApp(request):
    return render(request, "firstApp/index.html")