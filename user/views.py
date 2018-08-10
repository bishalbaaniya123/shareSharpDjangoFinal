from django.shortcuts import render


# Create your views here.
def homepage(request):
    return render(request, 'index.html')


def upload(request):
    if request.method == 'POST':
        pass
    else:
        return render(request, 'upload.html')


def upload2(request):
    return render(request, 'upload2.html')
