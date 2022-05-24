from django.shortcuts import render
import logging
logger = logging.getLogger('kdp_wb')

def company(request):
    logger.info("INFO 레벨로 출력")
    return render(request, 'kdp_wb/company.html')