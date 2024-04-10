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
          
        pass

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
      try:
          
        pass

      except Exception as e:
        return JsonResponse({'msg':str(e)})

    else:
        return JsonResponse({'msg':"method not supported"})


  except:
    return JsonResponse({'msg':"Unexpected error"})
