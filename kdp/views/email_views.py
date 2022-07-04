from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
import math
import random
import logging
import requests
import json
import datetime

logger = logging.getLogger('kdp')

# email sso 생성
@login_required(login_url='common:login')
def email(request):
    logger.info("INFO 레벨로 출력")
    hr = HttpResponse('ok')
    api_key = "#kdp@1914!"
    host_domain = "koreadigitalpark.com"
    user = User.objects.get(username=request.user)
    token = makeid()
    data = {"cid": user.username, "MailToken": token}
    context = {"api_key": api_key, "host_domain": host_domain, "data": data}
    json_data = json.dumps(context)
    expiry_time = datetime.datetime.now() + datetime.timedelta(seconds=10)
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    url = "https://mail.koreadigitalpark.com/mail_api/token_sso/"
    hr.set_cookie('MailToken', token, max_age=10, expires=expiry_time, path="/", domain=host_domain)
    requests.post(url, data=json_data, json=json_data, headers=headers)
    return redirect('https://mail.koreadigitalpark.com/lw_api/token_sso/' + token + '?return_url=')


# @login_required(login_url='common:login')
# def email(request):
#     logger.info("INFO 레벨로 출력")
#     hr = HttpResponse('ok')
#     api_key = "#kdp@1914!"
#     host_domain = "koreadigitalpark.com"
#     user = User.objects.get(username=request.user)
#     token = makeid()
#     data = {"cid": user.username, "MailToken": token}
#     context = {"api_key": api_key, "host_domain": host_domain, "data": data}
#     json_data = json.dumps(context)
#     expiry_time = datetime.datetime.now() + datetime.timedelta(seconds=10)
#     headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
#     url = "https://mail.koreadigitalpark.com/mail_api/token_sso/"
#     cookies = hr.set_cookie('MailToken', token, max_age=10, expires=expiry_time, path="/", domain=host_domain)
#     requests.post(url, data=json_data, json=json_data, headers=headers, cookies=cookies)
#     return render(request, 'kdp/email.html', context)



def makeid():
    text = ""
    possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    for i in range(0, 40):
        text += possible[math.floor(random.random() * len(possible))]
    return text
