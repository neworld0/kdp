from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import ClientAnswerForm
from ..models import Client, ClientAnswer, User

@login_required(login_url='common:login')
def client_answer_create(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    if request.method == "POST":
        form = ClientAnswerForm(request.POST)
        if form.is_valid():
            client_answer = form.save(commit=False)
            client_answer.author = request.user  # author 속성에 로그인 계정 저장
            client_answer.create_date = timezone.now()
            client_answer.client = client
            client_answer.save()
            return redirect('{}#client_answer_{}'.format(
                resolve_url('kdp_wb:client_detail', client_id=client.id), client_answer.id))
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'client': client, 'form': form}
    return render(request, 'kdp_wb/client_detail.html', context)

@login_required(login_url='common:login')
def client_answer_modify(request, client_answer_id):
    client_answer = get_object_or_404(ClientAnswer, pk=client_answer_id)
    if request.user != client_answer.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('kdp_wb:client_detail', client_id=client_answer.client.id)
    if request.method == "POST":
        form = ClientAnswerForm(request.POST, instance=client_answer)
        if form.is_valid():
            client_answer = form.save(commit=False)
            client_answer.modify_date = timezone.now()
            client_answer.save()
            return redirect('{}#client_answer_{}'.format(
                resolve_url('kdp_wb:client_detail', client_id=client_answer.client.id), client_answer.id))
    else:
        form = ClientAnswerForm(instance=client_answer)
    context = {'client_answer': client_answer, 'form': form}
    return render(request, 'kdp_wb/clientanswer_form.html', context)

@login_required(login_url='common:login')
def client_answer_delete(request, client_answer_id):
    client_answer = get_object_or_404(ClientAnswer, pk=client_answer_id)
    if request.user != client_answer.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        client_answer.delete()
    return redirect('kdp_wb:client_detail', client_id=client_answer.client.id)
