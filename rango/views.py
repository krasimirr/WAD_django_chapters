from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there world! <a href='/rango/about'> About page </a>")
	
def about(request):
    return HttpResponse("Rango says hey there world! <a href='/rango/'> Go back </a>")