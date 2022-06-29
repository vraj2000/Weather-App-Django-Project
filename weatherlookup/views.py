from django.shortcuts import render

# Create your views here.

def home(request):
    import json
    import requests
    api_request = requests.get("http://api.weatherapi.com/v1/current.json?key=2c5e0a4a94444d15b5b104506222606&q=London&aqi=no")

    try:
        api = json.loads(api_request.content)
    except  Exception as e:
        api = "Error"


    return render(request,'home.html',{'api':api})


def about(request):
    return render(request,'about.html',{})