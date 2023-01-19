from django.shortcuts import render
from urllib.request import urlopen
import json

# Create your views here.
def home(request):
    url="https://api.quotable.io/random"
    response=urlopen(url)
    data_json=json.loads(response.read())
    mydata=(data_json['content'])
    return render(request,'jokesapp/index.html',{'message':mydata})