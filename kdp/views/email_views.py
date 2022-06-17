from django.shortcuts import render
import logging
logger = logging.getLogger('kdp')

def email(request):
    logger.info("INFO 레벨로 출력")
    return render(request, 'kdp/email.html')