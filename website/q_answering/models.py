from django.db import models


class Question(models.Model):
    """
    A class representing parliamentary questions, their state and answer.

    The Question class contains information about a parliamentary question.
    It contains a title, displaying the question topic in max 40 characters,
    a short description of max 200 characters, an answer of unknown length
    that will be updated through the workspace, and a status that signifies
    the progress made of answering the question.
    """
    # A question title, will be displayed on the workspace screen
    title = models.CharField(max_length=40)
    # A question description, will pop up when question is clicked
    description = models.CharField(max_length=200)
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
