from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sessions import middleware
from django.http import HttpResponse
from django.http.response import HttpResponseBase
from django.shortcuts import render, redirect
from django.conf import settings
import math
import random
import logging
import requests
import json
import datetime
logger = logging.getLogger('kdp')

# @login_required(login_url='common:login')
# def email(request):
#     logger.info("INFO 레벨로 출력")
#     return render(request, 'kdp/email.html')


# email sso 생성
@login_required(login_url='common:login')
def email(request):
    logger.info("INFO 레벨로 출력")
    hr = HttpResponse('ok')
    api_key = "#kdp@1914!"
    host_domain = "koreadigitalpark.com"
    user = User.objects.get(username=request.user)
    token = makeid()
    data = {"MailToken": token, "cid": user.username}
    context = {"api_key": api_key, "host_domain": host_domain, "data": data}
    json_data = json.dumps(context)
    expiry_time = datetime.datetime.now() + datetime.timedelta(seconds=10)
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    url = "https://mail.koreadigitalpark.com/mail_api/token_sso/"
    cookie = hr.set_cookie('MailToken', token, max_age=10, expires=expiry_time, path="/", domain=host_domain)
    requests.post(url, data=json_data, headers=headers, cookies=cookie)
    return redirect('https://mail.koreadigitalpark.com/lw_api/token_sso/' + token + '?return_url=')


def makeid():
    text = ""
    possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    for i in range(0, 40):
        text += possible[math.floor(random.random() * len(possible))]
    return text
