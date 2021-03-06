from django.shortcuts import render
import requests
from django.http import HttpResponse,Http404,HttpResponseRedirect
import json
from django.shortcuts import render
from android.models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(title,text,sender):
    uids = []
    users = User.objects.all().order_by('-id')
    for user in users:
        uids.append(user.token)

    notis = Noti.objects.all().order_by('-id')
    noti = notis[0]
    url = 'https://gcm-http.googleapis.com/gcm/send'
    #payload = { "notification": {"title": title,"icon":"@drawable/myicon","text": text,"click_action":"MAIN"},"registration_ids" : uids}
    payload = {"data":{"message1":text,"title":title,"sender":sender},"registration_ids":uids}
    headers = {'content-type': 'application/json','Authorization':'key='+noti.api_key}
    
    print payload
    print headers
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    return json.loads(r.content)

@csrf_exempt
def register(request):
    if request.method == "POST" and request.POST['passkey'] == "hellolastry":
        u = User()
        u.name = request.POST["name"]
        u.token = request.POST["token"]
        u.email = request.POST["email"]
        u.phone_no = request.POST["phone_no"]
        u.image_url = request.POST["image_url"]
        u.social_id = request.POST["social_id"]
        u.role = ""
        u.save()
        return HttpResponse("User Registered")
    else:
        return HttpResponse("Validation Failed")


@csrf_exempt
def message_receive(request):
    if request.method == 'POST' and request.POST['passkey'] == 'hellolastry':
        try:
            x = User.objects.get(token=request.POST["token"])
        except:
            return HttpResponse("User not Registered")
        msg = Message()
        msg.sender = request.POST['username']
        msg.message = request.POST['bmsg']
        msg.token = request.POST["token"]
        data = home("Broadcast Message",msg.message)
        msg.message_id = data['multicast_id']
        msg.save()
        data["action"]="broadcast_msg"
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return HttpResponse("Validation Failed")

@csrf_exempt
def contacts_data(request):
    if request.method == 'POST' and request.POST['passkey'] == 'hellolastry':
        data = {"contacts":[],"action":"fetch_contacts"}
        users = User.objects.all().order_by('name')
        for user in users:
            user_dict = {}
            user_dict["name"] = user.name
            data["contacts"].append(user_dict)
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return HttpResponse("Validation Failed")

@csrf_exempt
def message_data(request):
    if request.method == 'POST' and request.POST['passkey'] == 'hellolastry':
        data = {"messages":[],"action":"fetch_messages"}
        messages = Message.objects.all().order_by('-id')
        for message in messages:
            msg_dict = {}
            msg_dict["sender"] = message.sender
            msg_dict["message"] = message.message
            data["messages"].append(msg_dict)
        return HttpResponse(json.dumps(data), content_type='application/json')
    else:
        return HttpResponse("Validation Failed")



