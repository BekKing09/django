from django.shortcuts import render, redirect
from main.models import Course
from django.http import HttpRequest
import requests

TOKEN = "8218998010:AAFAjzveRkI9bTKTQVywm1GpPjCNsEmaVj0"
CHAT_ID = "7152580871"

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
    return render(request, "main/index.html")

def about_devoloper(request):
    return render(request, "main/about.html")
