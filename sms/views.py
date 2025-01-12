import requests
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    api_url = "https://common.nenyon.com/v1/sms/"  
    try:
        response = requests.get(api_url,verify=False)
        #response.raise_for_status()  
        api_data = response.json() 
        return render(request, 'sms/index.html', {"messages": api_data})
    except requests.exceptions.RequestException as e:
        return HttpResponse(f"An error occurred while fetching data: {e}", status=500)



def messages(request):
    api_url = "https://common.nenyon.com/v1/sms/"  
    try:
        response = requests.get(api_url,verify=False)
        #response.raise_for_status()  
        api_data = response.json() 
        return render(request, 'sms/messages.html', {"messages": api_data})
    except requests.exceptions.RequestException as e:
        return HttpResponse(f"An error occurred while fetching data: {e}", status=500)


def reports(request):
    return render(request,'sms/reports.html')