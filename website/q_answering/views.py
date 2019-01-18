from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Subquestion, Article
from django.urls import reverse

def index(request):
    """ return the workspace main page """
    # acquire lists of all questions by status
    todo_questions          = Question.objects.filter(status='TD', answered=False)
    inprogress_questions    = Question.objects.filter(status='IP', answered=False)
    needverify_questions    = Question.objects.filter(status='NV', answered=False)
    approved_questions      = Question.objects.filter(status='AP', answered=False)

    # pass the question lists as context
    context = {
        'todo_questions': todo_questions,
        'inprogress_questions': inprogress_questions,
        'needverify_questions': needverify_questions,
        'approved_questions': approved_questions,
    }
    return render(request, 'q_answering/index.html', context)


def edit(request):
    """ return the question edit window """
    # here we want to call the IR/datascience function
    q_id = request.POST['id']
    current_question = Question.objects.get(pk=q_id)
    # pass question ID as context
    context = {
        'question_id': q_id,
        'current_question': current_question,
        'current_subquestions': current_question.subquestion_set.all(),
        'articles': Article.objects.all(),
        'oldquestions': Question.objects.filter(answered=True),
    }
    return render(request, 'q_answering/questioneditwindow.html', context)


def updateQuestion(request):
    """ return a redirect to the index page after updating question status """
    # get the question that is currently active
    question = get_object_or_404(Question, pk=request.POST['id'])
    # change the question status and answer and save this to the database
    question.status = request.POST['statusbtn']
    question.answer = request.POST['answer']
    question.save()

    return HttpResponseRedirect(reverse('index'))
