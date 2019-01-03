from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.urls import reverse

def index(request):
    """ return the workspace main page """
    # acquire lists of all questions by status
    todo_questions          = Question.objects.filter(status='TD')
    inprogress_questions    = Question.objects.filter(status='IP')
    needverify_questions    = Question.objects.filter(status='NV')
    approved_questions      = Question.objects.filter(status='AP')

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

    # pass question ID as context
    context = {
        'question_id': request.POST['id'],
    }
    return render(request, 'q_answering/questioneditwindow.html', context)


def updateQuestion(request):
    """ return a redirect to the index page after updating question status """
    # get the question that is currently active
    question = get_object_or_404(Question, pk=request.POST['id'])
    # change the question status and save this to the database
    question.status = request.POST['statusbtn']
    question.save()
    return HttpResponseRedirect(reverse('index'))
