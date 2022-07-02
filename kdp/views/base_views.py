from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import math
import logging
import socket
import requests
import re
logger = logging.getLogger(__name__)

def index(request):
    logger.info("INFO 레벨로 출력")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("kdigitalpark.kr", 443))
    print("내부 IP: ", sock.getsockname()[0])
    # req = requests.get("http://ipconfig.kr")
    # print("외부 IP: ", re.search(r'IP Address:(\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3})', req.text)[1])
    return render(request, 'kdp/index.html')



