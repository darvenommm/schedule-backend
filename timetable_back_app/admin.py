from django.contrib import admin

from .models import Audience, Group, GroupToStudent, Subject, Timetable, User


class GroupToStudent_inline(admin.TabularInline):
    model = GroupToStudent
    extra = 1


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    model = Subject


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    model = Group
    inlines = (GroupToStudent_inline,)


@admin.register(Audience)
class AudienceAdmin(admin.ModelAdmin):
    model = Audience


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    model = Timetable


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    inlines = (GroupToStudent_inline,)

