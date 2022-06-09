from django.shortcuts import render
import logging
logger = logging.getLogger(__name__)

def kdp_privacy_policy(request):
    logger.info("INFO 레벨로 출력")
    return render(request, 'kdp_wb/kdp_privacy_policy.html')

def korea_privacy_policy(request):
    logger.info("INFO 레벨로 출력")
    return render(request, 'kdp_wb/korea_privacy_policy.html')