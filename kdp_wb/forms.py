from django import forms
from kdp_wb.models import Question, Answer, Client, ClientAnswer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question  # 사용할 모델
        fields = ['subject', 'content']  # QuestionForm에서 사용할 Question 모델의 속성
        labels = {
            'subject': '제목',
            'content': '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }


class ClientAnswerForm(forms.ModelForm):
    class Meta:
        model = ClientAnswer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client  # 사용할 모델
        fields = ['email', 'content', 'name', 'company', 'phone', 'position', 'nation']  # ClientForm에서 사용할 Question 모델의 속성
        labels = {
            'email': '이메일',
            'phone': '전화번호',
            'name': '이름',
            'position': '직책',
            'company': '회사명',
            'nation': '국가',
            'content': '내용',
            'agree': '동의',
        }

# class SettingsForm(forms.ModelForm):
#     receive_newsletter = forms.BooleanField()

#     def __init__(self):
#         if check_something():
#             self.fields['receive_newsletter'].initial  = True

#     class Meta:
#         model = Settings

