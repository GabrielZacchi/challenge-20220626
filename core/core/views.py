from django.http import HttpResponse, HttpResponseNotFound
from rest_framework.decorators import api_view

@api_view(['GET'])
def index_view(request):
    return HttpResponse("Fullstack Challenge 20201026", status=200)