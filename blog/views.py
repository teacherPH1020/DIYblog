from django.shortcuts import render


# Create your views here.
def index_view(request):
    return render(request, "blog/index.html")

def login_view(request):
    return render(request, "blog/login.html")