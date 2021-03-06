from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.contrib.auth.models import User
from ..forms import ClientForm
from ..models import Client

# 고객 상담 문의
def contact(request):
    return render(request, 'kdp/client_form.html')


# 고객 상담 문의 목록 출력
@login_required(login_url='common:login')
def client(request):
    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬기준
    # 정렬
    if so == 'popular':
        client_list = Client.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', '-create_date')
    else:  # recent
        client_list = Client.objects.order_by('-create_date')
    # 검색
    if kw:
        client_list = client_list.filter(
            Q(email__icontains=kw) |  # 제목 검색
            Q(company__icontains=kw) |  # 회사 검색
            Q(content__icontains=kw)  # 문의 내용 검색
        ).distinct()
    # 페이징처리
    paginator = Paginator(client_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'client_list': page_obj, 'page': page, 'kw': kw}
    return render(request, 'kdp/client_list.html', context)


# Bulletin Board 상세내용 출력
@login_required(login_url='common:login')
def client_detail(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    context = {'client': client}
    return render(request, 'kdp/client_detail.html', context)


# Client 문의 접수 완료 화면
def client_receive(request):
    return render(request, 'kdp/client_receive.html')


# Client 문의 등록
def client_create(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        # form1 = SettingsForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            # selected = form1.save(commit=False)
            client.create_date = timezone.now()
            client.save()
            # selected = request.POST.getlist('selected')
            # selected.save()
            return redirect('kdp:receive')
    else:
        form = ClientForm()
    context = {'form': form} #,'form1': form1}
    return render(request, 'kdp/client_form.html', context)


# Client Board 질문 수정
@login_required(login_url='common:login')
def client_modify(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    if request.user != client.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('kdp:client_detail', client_id=client.id)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            client = form.save(commit=False)
            client.modify_date = timezone.now()  # 수정일시 저장
            client.save()
            return redirect('kdp:client_detail', client_id=client.id)
    else:
        form = ClientForm(instance=client)
    context = {'form': form}
    return render(request, 'kdp/client_form.html', context)


# Bulletin Board 질문 삭제
@login_required(login_url='common:login')
def client_delete(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    if request.user != client.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('kdp:client_detail', client_id=client.id)
    client.delete()
    return redirect('kdp:client')
