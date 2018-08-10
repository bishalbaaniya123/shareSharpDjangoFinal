from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import random

# Create your views here.
from user.models import PictureAll


def homepage(request):
    all_images = PictureAll.objects.all()
    all_images_list = []
    single_person = []
    for item in all_images:
        if item.person not in single_person:
            single_person.append(item.person)
            each_item = {}
            each_item['person'] = item.person
            each_item['url'] = item.url
            all_images_list.append(each_item)
            print("this is a single image", str(item.file))
    return render(request, 'index.html', {'list': all_images_list})


def upload(request):
    return render(request, 'upload.html')


@csrf_exempt
def upload_picture(request):
    print("this is the request in UPLOAD_PICTURE", request)
    all_people = ['bishal', 'anuj', 'dip', 'shailesh']
    pic = request.FILES['file']
    p = PictureAll()
    p.file = pic
    p.url = "images/gallery/" + pic.name.replace(" ", "_")
    p.person = random.choice(all_people)
    p.save()
    p.url = str(p.file)
    p.save()
    return HttpResponse('Image upload succeeded.')


def user_details(request, user_name):
    all_images = PictureAll.objects.all().filter(person=user_name)
    all_images_list = []
    for item in all_images:
        each_item = {}
        each_item['person'] = item.person
        each_item['url'] = item.url
        all_images_list.append(each_item)
    print("before render", all_images_list)
    return render(request, 'userDetails.html', {'list': all_images_list})
