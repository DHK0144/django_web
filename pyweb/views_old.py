from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse
from .models import Question, Answer, Comment
from .form import QuestionForm, AnswerForm, CommentForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    """
    pyweb 목록 출력
    """
    # page 입력 파라미터
    page = request.GET.get('page', '1') # page

    # 조회
    question_list = Question.objects.order_by('-create_date')

    # 페이징 처리
    paginator = Paginator(question_list, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}
    # context = {'question_list': question_list}
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









