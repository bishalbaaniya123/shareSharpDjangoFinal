from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from classifier.neuralnet import classifier_image
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


def receive(request):
    return render(request, 'receive.html')


@csrf_exempt
def upload_picture(request):
    print("this is the request in UPLOAD_PICTURE", request)
    pic = request.FILES['file']
    p = PictureAll()
    p.file = pic
    p.save()
    p.url = "./media/images/gallery/" + pic.name.replace(" ", "_")
    my_classifier = classifier_image(p.url)
    my_classifier.init_model()
    p.person = my_classifier.run_model()
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
    return render(request, 'userDetails.html', {'list': all_images_list, 'username': user_name})


def sendPic(request, lan, user_name):
    print("these is lan: ", lan, " this is username: ", user_name)
    # to get all images of that person
    all_images = PictureAll.objects.all().filter(person=user_name)
    # write your send function
    data = ["send_one", "send_two", "send_three"]
    return JsonResponse(data, safe=False)


def getListOfLans(request):
    data = ["one", "two", "three"]
    return JsonResponse(data, safe=False)
