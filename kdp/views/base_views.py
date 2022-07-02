from django.shortcuts import render
import logging
import socket

logger = logging.getLogger(__name__)

def index(request):
    logger.info("INFO 레벨로 출력")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("kdigitalpark.kr", 443))
    sockname = sock.getsockname()[0]
    context = {"Inner": sockname}
    return render(request, 'kdp/index.html', context)



