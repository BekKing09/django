from django.http import HttpResponse


def test_wiew(request):
    for i in range(10):
        print("yangi request")
    return HttpResponse("<h1>salom</h1>")