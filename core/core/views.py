from django.http import HttpResponse, HttpResponseNotFound


def index_view(request):
    return HttpResponse("Fullstack Challenge 20201026", status=200)