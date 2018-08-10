from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request, 'index.html')


def upload(request):
    return render(request, 'upload.html')
