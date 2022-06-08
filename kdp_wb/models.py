from django.db import models
from django.contrib.auth.models import User, Group
from django.shortcuts import reverse


class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)

    class Meta:
        permissions = [
            ('can_publish', 'Can Publish Posts'),
            ('can_change', 'Can Change Posts'),
            ('can_view', 'Can View Posts'),
            ('can_delete', 'Can Delete Posts'),
        ]
    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse("kdp_wb:question_list", kwargs={"pk": self.pk})


class Client(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    nation = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.email


class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')

    class Meta:
        permissions = [
            ('can_publish', 'Can Publish Posts'),
            ('can_change', 'Can Change Posts'),
            ('can_view', 'Can View Posts'),
            ('can_delete', 'Can Delete Posts'),
        ]

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse("kdp_wb:question_detail", kwargs={"pk": self.pk})