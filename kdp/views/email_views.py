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
# @login_required(login_url='common:login')
# def email(request):
#     logger.info("INFO 레벨로 출력")
#     hr = HttpResponse()
#     api_key = "#kdp@1914!"
#     host_domain = "koreadigitalpark.com"
#     user = User.objects.get(username=request.user)
#     token = makeid()
#     data = {"cid": user.username, "MailToken": token}
#     context = {"api_key": api_key, "host_domain": host_domain, "data": data}
#     json_data = json.dumps(context)
#     expiry_time = datetime.datetime.now() + datetime.timedelta(seconds=10)
#     headers = {
#         'Content-Type': 'application/x-www-form-urlencoded',
#         'Cookie': 'cisession=0a6224bbb7f9d1d1e710d20440da602094b6a347'
#     }
#     url = "https://mail.koreadigitalpark.com/mail_api/token_sso/"
#     cookies = hr.set_cookie("MailToken", token, max_age=10, expires=expiry_time, path="/", domain=host_domain)
#     requests.post(url, data=json_data, json=json_data, headers=headers, cookies=cookies)
#     return redirect('https://mail.koreadigitalpark.com/lw_api/token_sso/' + token + '?return_url=')

@login_required(login_url='common:login')
def email(request):
    logger.info("INFO 레벨로 출력")
    # user = User.objects.get(username=request.user)
    token = makeid()
    payload = 'api_key=%23kdp%401914!&host_domain=koreadigitalpark.com&data=%7B%22cid%22%3A%22kdp%22%2C%20%22MailToken%22%3A%22ZJbMIL2jwoJynEpk8wmXdlhj2e2aewvsS7VDZj9C%22%7D'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'cisession=0a6224bbb7f9d1d1e710d20440da602094b6a347'
    }
    url = "https://mail.koreadigitalpark.com/mail_api/token_sso/"
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    return redirect('https://mail.koreadigitalpark.com/lw_api/token_sso/' + token + '?return_url=')


def makeid():
    text = ""
    possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    for i in range(0, 40):
        text += possible[math.floor(random.random() * len(possible))]
    return text



# @login_required(login_url='common:login')
# def email(request):
#     logger.info("INFO 레벨로 출력")
#     return render(request, 'kdp/email.html')