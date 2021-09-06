from django.urls import path

from .views import base_views, question_views, answer_views, comment_views

app_name = 'pyweb'

urlpatterns = [
    # base_views.py
    path('',
         base_views.index, name='index'),
    path('<int:question_id>/',
         base_views.detail, name='detail'),

    # answer_views.py
    path('answer/create/<int:question_id>',
         answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/',
         answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/',
         answer_views.answer_delete, name='answer_delete'),

    # question_views.py
    path('question/create/',
         question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/',
         question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/',
         question_views.question_delete, name='question_delete'),

    # comment_views.py
    path('comment/create/question/<int:question_id>/',
         comment_views.comment_create_question, name='comment_create_question'),
    path('comment/modify/question/<int:question_id>/',
         comment_views.comment_modify_question, name='comment_modify_question'),
    path('comment/delete/question/<int:question_id>/',
         comment_views.comment_delete_question, name='comment_delete_question'),
    path('comment/create/question/<int:comment_id>/',
         comment_views.comment_create_question, name='comment_create_comment'),
    path('comment/modify/question/<int:comment_id>/',
         comment_views.comment_modify_question, name='comment_modify_comment'),
    path('comment/delete/question/<int:comment_id>/',
         comment_views.comment_delete_question, name='comment_delete_comment'),
]
