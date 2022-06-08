from django.urls import path

from .views import base_views, question_views, answer_views, vote_views, kdp_views, company_views, contact_views, client_views, client_answer_views, receive_views

app_name = 'kdp_wb'

urlpatterns = [
    # base_views.py
    path('',
         base_views.index, name='index'),

    # kdp_views.py
    path('kdp/', kdp_views.kdp, name='kdp'),

    # company_views.py
    path('company/', company_views.company, name='company'),

    # contact_views.py
    path('contact/', contact_views.contact, name='contact'),

    # client_views.py
    path('client/', client_views.client, name='client'),
    path('client/<int:client_id>/',
         client_views.client_detail, name='client_detail'),
    path('client/create/',
         client_views.client_create, name='client_create'),
    path('client/modify/<int:client_id>/',
         client_views.client_modify, name='client_modify'),
    path('client/delete/<int:client_id>/',
         client_views.client_delete, name='client_delete'),

    # receive_views.py
    path('receive/', receive_views.receive, name='receive'),


    # question_views.py
    path('question/', question_views.question, name='question'),
    path('question/<int:question_id>/',
         question_views.detail, name='detail'),
    path('question/create/',
         question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/',
         question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/',
         question_views.question_delete, name='question_delete'),

    # answer_views.py
    path('answer/create/<int:question_id>/',
         answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/',
         answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/',
         answer_views.answer_delete, name='answer_delete'),


    # client_answer_views.py
    path('client_answer/create/<int:client_id>/',
         client_answer_views.client_answer_create, name='client_answer_create'),
    path('client_answer/modify/<int:client_answer_id>/',
         client_answer_views.client_answer_modify, name='client_answer_modify'),
    path('client_answer/delete/<int:client_answer_id>/',
         client_answer_views.client_answer_delete, name='client_answer_delete'),

# vote_views.py
    path('vote/question/<int:question_id>/', vote_views.vote_question, name='vote_question'),
    path('vote/answer/<int:answer_id>/', vote_views.vote_answer, name='vote_answer'),
]
