from django.shortcuts import render
import requests
from django.http import HttpResponse,Http404,HttpResponseRedirect
import json
from django.shortcuts import render
from android.models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(title,text):
    uids = []
    users = User.objects.all().order_by('-id')
    for user in users:
        uids.append(user.token)

    notis = Noti.objects.all().order_by('-id')
    noti = notis[0]
    url = 'https://gcm-http.googleapis.com/gcm/send'
    payload = { "notification": {"title": title,"icon":"@drawable/myicon",text: "App chalana"},"registration_ids" : uids}
    headers = {'content-type': 'application/json','Authorization':'key='+noti.api_key}
    
    print payload
    print headers
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print r.content

@csrf_exempt
def register(request):
	if request.method == "POST" and request.POST['passkey'] == "hellolastry":
		u = User()
		u.name = request.POST["name"]
		u.token = request.POST["token"]
		u.save()
		return HttpResponse("User Registered")
	else:
		return HttpResponse("Validation Failed")


@csrf_exempt
def message_receive(request):
    if request.method == 'POST' and request.POST['passkey'] == 'hellolastry':
        msg = Message()
        msg.sender = request.POST['username']
        msg.message = request.POST['bmsg']
        msg.sender_id = request.POST['token']
        msg.save()
        return HttpResponse("message_recieved")
