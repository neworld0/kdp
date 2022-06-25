from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import math
import logging
logger = logging.getLogger(__name__)

def index(request):
    logger.info("INFO 레벨로 출력")
    return render(request, 'kdp/index.html')


# # email sso 생성
# @login_required(login_url='common:login')
# def email(request):
#     user = User.objects.get(username=request.user)
#     token = makeid()
#     context = {"cid": user, "MailToken": token}
#     return render(request, 'http://mail.koreadigitalpark.com/mail_api/token_sso', context)
#
#
# def makeid():
#     text = ""
#     possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
#     for i in range(0, 40):
#         text += possible.charAt(math.floor(math.random() * possible.length))
#     return text
