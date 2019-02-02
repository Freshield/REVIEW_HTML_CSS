from django.shortcuts import render, redirect
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    return render(request, 'contest.html')

def contest_res(request):
    if request.method == 'POST':
        print(request.POST)
        return HttpResponse('success')
    else:
        return redirect('/')

def coffee(request):
    if request.method == 'POST':
        print(dict(request.POST))
        return HttpResponse(json.dumps(dict(request.POST), indent=4))
    else:
        return render(request, 'coffee.html')

def sample(request):
    if request.method == 'POST':
        print(dict(request.POST))
        return HttpResponse(json.dumps(dict(request.POST), indent=4))
    else:
        return render(request, 'styledform.html')

def test_http(request):
    if request.method == 'POST':
        print(dict(request.POST))
        return HttpResponse("success")
    else:
        return HttpResponse('get')