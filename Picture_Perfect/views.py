# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from utility import adjustment


def to_plain(cipher_text):
    to_do = []
    attributes = {'vertical_ax_rot': 'Rotate along vertical axis by 15*',
                    'horiz_ax_rot': 'Rotate along horizontal axis by 15*',
                    'rotate': 'Rotate along --- ',
                    'zoom': 'Zoom by 25%',
                    'bright': 'Alter brightness of object'
                    }
    for att in attributes.keys():
        pos = eval_attr(cipher_text, att)
        if pos!=-1:
            res = attributes[att]
            if cipher_text[pos]=='+':
                res += ' on positive scale'
            elif cipher_text[pos]=='-':
                res += ' on negative scale'
            to_do.append(res)

    # print('Input: ', cipher_text)
    # for i in to_do:
    #     print(i)

    return '\n'.join(to_do)

def eval_attr(s='', attribute=''):
    x = s.find(attribute)
    if x==-1:
        return -1
    return x + len(attribute)

def home(request):
    optimisation = {
        'method': 'Optimisation menthod(s)',
        'score': '1'
        }
    try:
        img = request.FILES['image_input']
        res = adjustment.cam_adjustment(img)
        # print('='*70)
        # print('To API: ', res)
        optimisation['method'] = to_plain(res[0])
        optimisation['score'] = str(res[1])
    except Exception as e:
      pass
    return JsonResponse(optimisation)

def expanded_img(request):
    predictions = [0]*8
    try:
        img = request.FILES['input_image']
        predictions = [1]*8
    except:
        pass
    return JsonResponse({'predictions': predictions})