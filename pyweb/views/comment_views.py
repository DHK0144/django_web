from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..form import CommentForm
from ..models import Question, Comment


@login_required(login_url='pyweb:login')
def comment_create_question(request, question_id):
    """
    질문 댓글 등록
    """
    question = get_object_or_404(Question, pk=question_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.question = question
            comment.save()
            return redirect('pyweb:detail', question_id=question.id)
    else:
        form = CommentForm()

    context = {'form': form}
    return render(request, 'pyweb/comment_form.html', context)


@login_required(login_url='pyweb:login')
def comment_modify_question(request, comment_id):
    """
    질문 댓글 수정
    """
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author != request.user:
        messages.error("권한이 없습니다.")
        return redirect('pyweb:detail', comment.question.id)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('pyweb:detail', question_id=comment.question.id)

    else:
        form = CommentForm(instance=comment)

    context = {'form': form}
    return render(request, 'pyweb/comment_form.html', context)


@login_required(login_url='pyweb:login')
def comment_delete_question(request, comment_id):
    """
    질문 댓글 삭제
    """
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author != request.user:
        messages.error("삭제 권한이 없습니다.")
    else:
        comment.delete()

    return redirect('pyweb:detail', question_id=comment.question.id)









