from django.shortcuts import render
from live.models import Live

import shutil
import os
import json
from django.http import JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def link(request):
  try:   

    if request.method == "POST":
      try:
          
        pass

      except Exception as e:
        return JsonResponse({'msg':str(e)})

    else:
        return JsonResponse({'msg':"method not supported"})


  except:
    return JsonResponse({'msg':"Unexpected error"})




















@csrf_exempt
def stream(request):
  try:   

    if request.method == "POST":
      try:
          
        pass

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
          
        pass

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

