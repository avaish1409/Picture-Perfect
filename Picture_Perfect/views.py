# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from utility import adjustment

def home(request):
  img = request.get['Image']
  res = adjustment.cam_adjustment(img)
  print('='*70)
  print('To API: ', res)
  method = res[0]
  score = res[1]
  text = f'Method: {method}, Score: {Score}'
  return HttpResponse(text)
