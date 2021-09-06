from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..form import QuestionForm
from ..models import Question


@login_required(login_url='common:login')
def question_create(request):
    """
    질문 폼
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user  # 답변등록한 User 등록
            question.create_date = timezone.now()
            question.save()
            return redirect('pyweb:index')
        else:
            pass
    else:
        form = QuestionForm()

    context = {'form': form}
    return render(request, 'pyweb/question_form.html', context)


@login_required(login_url='common:login')
def question_modify(request, question_id):
    """
    질문 수정
    """

    question = get_object_or_404(Question, pk=question_id)

    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다.')
        return redirect('pyweb:detail', question_id=question_id)

    if request.method == "POST":
        # instance 넣어줘야 기존 내용이 들어가 있음
        # instance 기준으로 Form생성하지만 request.POST값으로 덮어쓰라
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            # 위에 form으로 받아온것들은 자동으로 들어가고 밑에서 modify_date가 들어가야하기 떄문에 commit False
            question = form.save(commit=False)
            question.modify_date = timezone.now()
            question.save()
            return redirect('pyweb:detail', question_id=question_id)
    else:
        # instance 넣어줘야 기존 내용이 들어가 있음
        form = QuestionForm(instance=question)

    context = {'form': form}
    return render(request, 'pyweb/question_form.html', context)


@login_required(login_url='common:login')
def question_delete(request, question_id):
    """
    질문 삭제
    """
    question = get_object_or_404(Question, pk=question_id)

    if request.user != question.author:
        messages.error("삭제할 권한이 없습니다.")
        return redirect('pyweb:detail', question_id=question_id)

    question.delete()
    return redirect('pyweb:index')









