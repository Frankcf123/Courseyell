from django.http import HttpResponse
from django.shortcuts import render
from Courseyell import settings
# Create your views here.
def index(request):
    # user = request.user
    return render(request, 'index.html')


