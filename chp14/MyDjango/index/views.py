from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'contest.html')

def contest_res(request):
    if request.method == 'POST':
        print(request.POST)
        return HttpResponse('success')
    else:
        return redirect('/')
