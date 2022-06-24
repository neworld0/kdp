from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import logging
logger = logging.getLogger('kdp')

# def email(request):
#     logger.info("INFO 레벨로 출력")
#     return render(request, 'kdp/email.html')


# Bulletin Board 상세내용 출력
@login_required(login_url='common:login')
def email(request, ):
    user = User.objects.get(username=request.user)
    context = {'cid': user, "MailToken": "0SF4RVoz51hPaa37sCYJdftrpk91eL6hBAKWzq3n"}
    return render(request, 'kdp/email.html', context)
