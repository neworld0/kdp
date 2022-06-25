from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
import math
import random
import logging
import requests
import json
logger = logging.getLogger('kdp')

@login_required(login_url='common:login')
def email(request):
    logger.info("INFO 레벨로 출력")
    return render(request, 'kdp/email.html')


# # email sso 생성
# @login_required(login_url='common:login')
# def email(request):
#     token = ''
#     user = User.objects.get(username=request.user)
#     token = makeid()
#     context = {"MailToken": token, "cid": user.username}
#     return render(request, 'kdp/email.html', context)
#
# def makeid():
#     text = ""
#     possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
#     for i in range(0, 40):
#         text += possible[math.floor(random.random() * len(possible))]
#     return text
