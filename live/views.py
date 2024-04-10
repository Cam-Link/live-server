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
