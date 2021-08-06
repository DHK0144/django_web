from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse
from .models import Question
from .form import QuestionForm, AnswerForm


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
    # question = Question.objects.get(id=question_id)
    # question_id 가 없을 경우 404 return
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pyweb/question_detail.html', context)
# Create your views here.


def answer_create(request, question_id):
    """
    답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pyweb:detail', question_id=question.id)
        else:
            pass
    else:
        form = AnswerForm()

    context = {'question': question, 'form': form}
    return render(request, 'pyweb/question_detail.html', context)
    # question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    # return redirect('pyweb:detail', question_id=question_id)


def question_create(request):
    """
    질문 폼
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pyweb:index')
        else:
            pass
    else:
        form = QuestionForm()

    context = {'form': form}
    return render(request, 'pyweb/question_form.html', context)













