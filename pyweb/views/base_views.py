from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

from ..models import Question


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










