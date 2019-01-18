from django.db import models


class Question(models.Model):
    """
    A class representing parliamentary questions, their state and answer.
    """
    # A question id, which corresponds to the ID's used by the ministry.
    question_id = models.CharField(max_length=50)
    # A boolean that keeps track of whether a question is answered or not.
    answered = models.BooleanField(default=False)
    upload_date = models.DateTimeField()
    title = models.CharField(max_length=50)
    # A question description, will pop up when question is clicked.
    description = models.CharField(max_length=200)
    # A relative link to the question pdf document
    question_document = models.CharField(max_length=200)
    # A question answer, will be updated as people save their answer
    # to the question after having worked on it in the workspace.
    answer = models.TextField(blank=True)

    # Each Question has a status, defining the amount of progress
    # that has been made into answering it.
    TODO = 'TD'
    INPROGRESS = 'IP'
    NEEDVERIFY = 'NV'
    APPROVED = 'AP'
    STATUS_CHOICES = (
        (TODO, 'Nieuw'),
        (INPROGRESS, 'Mee Bezig'),
        (NEEDVERIFY, 'Afgerond'),
        (APPROVED, 'Goedgekeurd'),
    )
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=TODO,
    )

    def __str__(self):
        return self.title


class Article(models.Model):
    """
    Article
    """
    title = models.CharField(max_length=50)
    article_document = models.CharField(max_length=200)
    SCIENTIFIC = 'SCI'
    NEWS = 'NEW'
    LAW = 'LAW'
    TYPE_CHOICES = (
        (SCIENTIFIC, 'onderzoek'),
        (NEWS, 'nieuws'),
        (LAW, 'wet'),
    )
    article_type = models.CharField(
        max_length=3,
        choices=TYPE_CHOICES,
        default=NEWS,
    )

    def __str__(self):
        return self.title


class Employee(models.Model):
    """
    Employee
    """
    is_admin = models.BooleanField(default=False)
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.user_name


class Activity(models.Model):
    """
    Activity
    """
    # Employee who has executed the activity
    executing_employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    # Question that is targeted with the activity
    target_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    date = models.DateTimeField()
    # Type of activity: a move (a change of status) of the question, an
    # alteration of the question answer, or an approval
    MOVE = 'MV'
    ALTERED = 'AL'
    APPROVED = 'AP'
    ACTIVITY_CHOICES = (
        (MOVE, 'verplaatst'),
        (ALTERED, 'geweizigd'),
        (APPROVED, 'goedgekeurd'),
    )
    activity_type = models.CharField(
        max_length=2,
        choices=ACTIVITY_CHOICES,
        default=ALTERED,
    )

    def __str__(self):
        return "{} -> {}({})".format(self.executing_employee,
                                self.activity_type, self.target_question)


class Subquestion(models.Model):
    """
    Subquestion
    """
    parent_question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content


class Verification(models.Model):
    """
    Verification
    """
    executing_employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    target_question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return "{} -verified-> {}".format(self.executing_employee,
                                    self.target_question)
