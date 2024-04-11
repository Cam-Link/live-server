from django.shortcuts import render
from live.models import Live

import shutil
import os
import json
from django.http import JsonResponse, FileResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sessions.backends.db import SessionStore


# Create your views here.

@csrf_exempt
def link(request):
  try:
    if request.method == 'POST':
      try:
        code = request.POST.get('code')

        user = Live.objects.create(number=0, code=code)

        session = SessionStore()

        session['user_id'] = user.id
        session.create()

        user_folder = os.path.join('videos', str(user.id))
        os.makedirs(user_folder)

        response = JsonResponse({'msg' : 'success'})
        response.set_cookie('session_id', session.session_key)

        return response
      
      except Exception as e:
        return JsonResponse({'msg':str(e)})

  except:
    return HttpResponse('Method not allowed', status=405)

















@csrf_exempt
def stream(request):
  try:   

    if request.method == "POST":
      try:
          
        chunk = request.FILES['chunk']

        id = request.session.get("uid")

        number = Live.objects.filter(id = id)[0].number

        path1 = os.getcwd() + f"/live/videos/{id}/{number}.webm"

        with open(path1,'ab') as video:
                video.write(chunk.read())

          

        number = number + 1
        number.save()



        return JsonResponse({'msg':'success'})

      except Exception as e:
        return JsonResponse({'msg':str(e)})

    else:
        return JsonResponse({'msg':"method not supported"})


  except:
    return JsonResponse({'msg':"Unexpected error"})























@csrf_exempt
def refresh(request):
  try:   

    if request.method == "POST":
      try:

        users = Link.objects.all()

        live_hosts = []

        for i in users:
          live_hosts.insert(0,i.id)

        if live_hosts == []:
          return JsonResponse({'msg':'no new link'})

        return JsonResponse({'msg':'success','live':live_hosts})

      except Exception as e:
        return JsonResponse({'msg':str(e)})

    else:
        return JsonResponse({'msg':"method not supported"})


  except:
    return JsonResponse({'msg':"Unexpected error"})




















@csrf_exempt
def play(request):
  try:   

    if request.method == "POST":
      try:
          
        data = json.loads(request.body)

        uid = data['uid']
        cid = data['cid']

        #return the requested chunk of video
        
        
        path = os.getcwd() + f"/live/videos/{uid}/{cid}.webm"

        chunk = open(path, 'rb')

        return FileResponse(chunk, content_type='video/webm')

      except Exception as e:
        return JsonResponse({'msg':str(e)})

    else:
        return JsonResponse({'msg':"method not supported"})


  except:
    return JsonResponse({'msg':"Unexpected error"})



















@csrf_exempt
def stop(request):
  try:
    if request.method == "POST":
      
      uid = request.session.get('uid')
      
      #Delete User
      Live.objects.filter(id=uid)[0].delete()
      
      #Delete folder based on User ID name
      shutil.rmtree(os.getcwd() + f"/live/videos/{uid}")
      
      return JsonResponse({'msg': 'success'})
        
    
    else:
      return JsonResponse({'error': 'Method is not allowed.'}, status=405)
  
  except Exception as e:
    return JsonResponse({'error': 'Unexpected error', 'details': str(e)}, status=500)

