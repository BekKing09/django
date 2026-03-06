from django.shortcuts import render, redirect
from main.models import Course
from django.http import HttpRequest
import requests

TOKEN = ""
CHAT_ID = ""

def index_view(request: HttpRequest):
    if request.method == "POST":
        course_name = request.POST.get("course_name", "Unknown")
        course_price = request.POST.get("course_price", 0)
        discount_type = request.POST.get("discount_type", "flex")
        discount = request.POST.get("discount", 0)
        course = Course.objects.create(
            title=course_name,
            price=course_price,
            discount_type=discount_type,
            discount=discount
        )
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

        text = f"Yangi kurs yaratildi sayt orqali\nKurs nomi: {course_name}\nKurs narxi: {course_price}"

        requests.get(url=url, params={
            "chat_id": CHAT_ID,
            "text": text
        })

        return redirect("index")
    courses = Course.objects.all()

    search = request.GET.get("search", None)

    price_from = request.GET.get("price_from", None)
    price_to = request.GET.get("price_to", None)
    if price_from or price_to:
        courses = Course.objects.filter(price__gte=price_from, price__lte=price_to)
    if search:
        courses = Course.objects.filter(title__icontains=search)

    context = {
        "courses": courses,
        "search": search if search else ""
    }
    return render(request, "main/index.html", context)

def about_devoloper(request):
    return render(request, "main/about.html")



