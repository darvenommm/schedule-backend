from datetime import datetime, timezone
from uuid import uuid4

from django.conf.global_settings import AUTH_USER_MODEL
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)

    class Meta:
        abstract = True


class CreatedMixin(models.Model):
    created = models.DateTimeField(
        _('created'), default=datetime.now, blank=True, null=False)

    class Meta:
        abstract = True


class ModifiedMixin(models.Model):
    modified = models.DateTimeField(
        _('modified'), default=datetime.now, blank=True, null=False)

    class Meta:
        abstract = True


# class User(UUIDMixin, CreatedMixin, ModifiedMixin):
#     teacher = 'лекция'
#     student = 'студент'
#     CHOICES = (
#               (teacher, 'учитель'),
#               (student, 'студент'),
#     )
#     role = models.CharField(_('role'), max_length=40, choices=CHOICES)
#     user_name = models.CharField(
#         _('user name'), max_length=40)
#     user_surname = models.CharField(
#         _('user surname'), max_length=40)
#     email = models.EmailField(_('email'), blank=True, null=True)
#     user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
#     subject = models.ForeignKey(
#         'Subject', on_delete=models.CASCADE, blank=True, null=True)
#     group = models.ForeignKey(
#         'Group', on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.user_surname} {self.user_name}"

#     class Meta:
#         db_table = 'user'
#         verbose_name = _('user')
#         verbose_name_plural = _('users')

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    created_by = models.DateTimeField(default=timezone.now)
    modified_by = models.DateTimeField(default=timezone.now)
    role = models.CharField(max_length=100, default="normal")
    status = models.CharField(max_length=100, default="Active")
    auth_provider = models.CharField(
        max_length=50, blank=True, default='email')

class Subject(UUIDMixin, CreatedMixin, ModifiedMixin):
    usual = 'лекция'
    lab = 'лабораторная'
    CHOICES = (
              (usual, 'лекция'),
              (lab, 'лабораторная'),
    )
    title = models.CharField(_('title'), max_length=40)
    kind = models.CharField(_('title'), max_length=40, choices=CHOICES)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = 'subject'
        verbose_name = _('subject')
        verbose_name_plural = _('subjects')


class Group(models.Model):
    name = models.CharField(_('name'), max_length=20, unique=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _('group')
        verbose_name_plural = _('groups')


class Audience(models.Model):
    usual = 'стандартная'
    lab = 'лаборатория'
    CHOICES = (
              (usual, 'стандартная'),
              (lab, 'лаборатория'),
    )
    name = models.CharField(max_length=20, unique=True)
    kind = models.CharField(
        _('kind'), max_length=20, choices=CHOICES, default=usual)

    def __str__(self):
        return f"{self.name} {self.kind}"

    class Meta:
        verbose_name = _('audience')
        verbose_name_plural = _('audiences')


class Timetable(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    audience = models.ForeignKey(Audience, on_delete=models.CASCADE)
    numb = models.CharField(_('numb'), max_length=20)
    day = models.DateTimeField(
        _('day'), blank=False, null=False)


    def __str__(self):
        return f"{self.group} - {self.subject} - {self.day}"

    class Meta:
        verbose_name = _('timetable')
        verbose_name_plural = _('timetable')


class GroupToStudent(UUIDMixin, CreatedMixin):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'group_to_student'
        unique_together = (('group', 'student'),)
