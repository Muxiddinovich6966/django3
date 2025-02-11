from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>App 3dan salom</h1>')
def about(request):
    return HttpResponse('<h1>App 3 about dan salom</h1>')
def test(request):
    return HttpResponse('<h1>App 3 test dan salom</h1>')