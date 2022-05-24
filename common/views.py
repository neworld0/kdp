from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.shortcuts import render, redirect, resolve_url, HttpResponse, get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from common.forms import UserForm


# 계정 생성
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})


@login_required(login_url='common:login')
def profile(request, user_id):
    user = User.objects.get(id=user_id)
    groups = user.groups.all()
    context = {'groups': groups}
    return render(request, 'common/profile.html', context)


def page_not_found(request, exception):
    """
    404 Page not found
    """
    return render(request, 'common/404.html', {})


def internal_server_error(request, *args, **argv):
    """
    500 Internal Server Error
    """
    return render(request, 'common/500.html', status=500)


class MyPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('common:profile')
    template_name = 'common/password_change_form.html'

    def form_valid(self, form):
        messages.info(self.request, '암호 변경을 완료했습니다.')
        return super().form_valid(form)


class MyPasswordResetView(PasswordResetView):
    success_url = reverse_lazy('common:login')
    template_name = 'common/password_reset_form.html'
    email_template_name = 'common/password_reset.html'

    def form_valid(self, form):
        messages.info(self.request, '암호 변경 메일을 발송했습니다.')
        return super().form_valid(form)


class MyPasswordResetConfirmView(PasswordResetConfirmView):
    success_url = reverse_lazy('common:login')
    template_name = 'common/password_reset_confirm.html'

    def form_valid(self, form):
        messages.info(self.request, '암호 초기화를 완료했습니다.')
        return super().form_valid(form)