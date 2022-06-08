from django.contrib import admin
from .models import Question, Answer, Client, ClientAnswer

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)


class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['content']

admin.site.register(Answer, AnswerAdmin)


class ClientAdmin(admin.ModelAdmin):
    search_fields = ['email']

admin.site.register(Client, ClientAdmin)


class ClientAnswerAdmin(admin.ModelAdmin):
    search_fields = ['content']

admin.site.register(ClientAnswer, ClientAnswerAdmin)