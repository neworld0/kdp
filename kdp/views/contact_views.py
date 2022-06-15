from django.shortcuts import render
import logging
logger = logging.getLogger('kdp')

def contact(request):
    logger.info("INFO 레벨로 출력")
    return render(request, 'kdp/contact.html')