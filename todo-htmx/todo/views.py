from django.shortcuts import render


def home(request):
    return render(request, "pages/home.html")


def auth(request):
    return render(request, "components/auth.html")
