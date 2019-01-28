from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Subquestion, Article, Verification, Employee, OldQuestion
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
    q_id = request.POST['id']
    current_question = Question.objects.get(pk=q_id)
    # here we want to call the IR/datascience function
    # pass question ID as context
    context = {
        'question_id': q_id,
        'current_question': current_question,
        'current_subquestions': current_question.subquestion_set.all(),
        'articles': [Article.objects.get(pk=1),
                     Article.objects.get(pk=5),
                     Article.objects.get(pk=7),
                     ],
        'oldquestions': [OldQuestion.objects.get(pk=1),
                         OldQuestion.objects.get(pk=5),
                         OldQuestion.objects.get(pk=7),
                         ],
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


def updateApproval(request):
    """ update the approval of a question and refresh the index page"""
    question = get_object_or_404(Question, pk=request.POST['questionid'])
    employee = get_object_or_404(Employee, pk=request.POST['employeeid'])
    question.verification_set.create(executing_employee=employee)
    question.status = "AP"
    question.save()

    return HttpResponseRedirect(reverse('index'))
