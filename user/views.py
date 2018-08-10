from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from user.models import PictureAll


def homepage(request):
    return render(request, 'index.html')


def upload(request):
    return render(request, 'upload.html')


@csrf_exempt
def upload_picture(request):
    pic = request.FILES['file']
    p = PictureAll()
    p.file = pic
    p.url = "images/gallery/" + pic.name.replace(" ", "_")
    p.save()
    p.url = str(p.file)
    p.save()
    return HttpResponse('Image upload succeeded.')
