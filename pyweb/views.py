from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse
from .models import Question


def index(request):
    """
    pyweb 목록 출력
    """
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list': question_list}
    return render(request, 'pyweb/question_list.html', context)

    # return HttpResponse("Welcome django web")


def detail(request, question_id):
    """
    detail 출력내용
    """
    # question_detail = Question.objects.get(id=question_id)
    # question_id 가 없을 경우 404 return
    question_detail = get_object_or_404(Question, pk=question_id)
    context = {'question_detail': question_detail}
    return render(request, 'pyweb/question_detail.html', context)
# Create your views here.


def answer_create(request, question_id):
    """
    답변 폼
    """
    question = get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content', create_date=timezone.now()))
    return redirect('pyweb:detail', question_id=question_id)
