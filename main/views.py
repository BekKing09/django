from django.shortcuts import render


def index_view(request):
    return render(request, "main/index.html")

def about_devoloper(request):
    return render(request, "main/about.html")
