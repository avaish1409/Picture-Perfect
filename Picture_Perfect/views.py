# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from utility import adjustment


res = adjustment.cam_adjustment('/home/anirudh/Desktop/aov.png')
print('='*70)
print('To API: ', res)