from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>App 2 dan salom</h1>')

def about(request):
    return HttpResponse('<h1>App 2 about dan salom</h1>')

def test(request):
    return HttpResponse('<h1>App 2 test dan salom</h1>')