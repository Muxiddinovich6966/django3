from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Salom project 1 dagi app 1</h1>')

def about(request):
    return HttpResponse('<i>About view</i>')

def test(request):
    return HttpResponse('<i>Test view</i>')