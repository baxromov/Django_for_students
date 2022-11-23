from django.contrib import admin
from students.models import Student, Course


# Register your models here.


# admin.site.register(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'first_name',
        'last_name',
        'course',
        'birth_date',
        'gender',
        'email',
        'created_at',
        'update_at'
    ]
    list_display_links = [
        'id',
        'first_name',
        'last_name',
    ]
    search_fields = [
        'id',
        'first_name',
        'last_name',
        'email',
    ]
    list_filter = [
        'gender',
        'course'
    ]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']

# admin.site.register(Student, StudentAdmin)
