from django.contrib import admin

from .models import Students, Teachers, TeacherStudent, Compositions, StudentComposition, Instruments


class CompositionsModelAdmin(admin.ModelAdmin):
    model = Compositions


class TeachersInstanceInline(admin.TabularInline):
    model = TeacherStudent


class StudentsInstanceInline(admin.TabularInline):
    model = TeacherStudent


class StudentsModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'updated']
    inlines = [StudentsInstanceInline]

    class Meta:
        model = Students


class TeachersModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'updated']
    inlines = [TeachersInstanceInline]

    class Meta:
        model = Teachers


class TeacherStudentModelAdmin(admin.ModelAdmin):
    list_display = ['teacher', 'student']

    class Meta:
        model = TeacherStudent


class InstrumentsModelAdmin(admin.ModelAdmin):
    list_display = ['name']

    class Meta:
        model = Instruments


admin.site.register(Students, StudentsModelAdmin)
admin.site.register(Teachers, TeachersModelAdmin)
admin.site.register(TeacherStudent, TeacherStudentModelAdmin)
admin.site.register(Instruments, InstrumentsModelAdmin)
