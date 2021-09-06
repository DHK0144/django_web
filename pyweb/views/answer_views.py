from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..form import AnswerForm
from ..models import Question, Answer


@login_required(login_url='common:login')
def answer_create(request, question_id):
    """
    답변등록
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user # 답변등록한 User 등록
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


@login_required(login_url='pyweb:login')
def answer_modify(request, answer_id):
    """
    질문 수정
    """
    answer = get_object_or_404(Answer, pk=answer_id)

    if request.user != answer.author:
        messages.error("삭제할 권한이 없습니다.")
        return redirect('pyweb:detail', question_id=answer.question.id)

    if request.method == 'POST':
        form = AnswerForm(request.POST, instance=answer)

        if form.is_valid():
            form.save(commit=False)
            answer.modify_date = timezone.now()
            answer.save()
            return redirect('pyweb:detail', question_id=answer.question.id)

    else:
        form = AnswerForm(instance=answer)

    context = {'answer': answer, 'form': form}
    return render(request, 'pyweb/answer_form.html', context)


@login_required(login_url='pyweb:login')
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)

    if request.user != answer.author:
        messages.error("권한이 없습니다.")
        return redirect('pyweb:detail', question_id=answer.question.id)

    answer.delete()
    return redirect('pyweb:detail', question_id=answer.question.id)




