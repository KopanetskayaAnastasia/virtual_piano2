from django.db import models
from django.contrib.auth.models import User


class Instruments(models.Model):
    name = models.CharField(verbose_name='Название инструмента', max_length=100)

    def __str__(self):
        return self.name

    def get_pk(self):
        return self.pk

    class Meta:
        verbose_name = 'Инструмент'
        verbose_name_plural = 'Инструменты'


class Teachers(models.Model):
    name = models.CharField(verbose_name='Фио', max_length=100)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    email = models.EmailField(verbose_name='Почтовый адрес', max_length=100)
    created_at = models.DateTimeField(verbose_name='Дата регистрации', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Дата обновления', auto_now=True, auto_now_add=False)
    instrument = models.ForeignKey(Instruments, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    def get_pk(self):
        return self.pk

    def get_absolute_url(self):
        return f'/users/{self.id}'

    class Meta:
        verbose_name = 'Учитель'
        verbose_name_plural = 'Учителя'


class Students(models.Model):
    name = models.CharField(verbose_name='Фио', max_length=100)
    email = models.EmailField(verbose_name='Почтовый адрес', max_length=100)
    grade_of_school = models.IntegerField(verbose_name='Год обучения')
    created_at = models.DateTimeField(verbose_name='Дата регистрации', auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Дата обновления', auto_now=True, auto_now_add=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    instrument = models.ForeignKey(Instruments, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    def get_pk(self):
        return self.pk

    def get_absolute_url(self):
        return f'/users/{self.id}'

    class Meta:
        verbose_name = 'Ученик'
        verbose_name_plural = 'Ученики'


class TeacherStudent(models.Model):
    teacher = models.ForeignKey(Teachers, on_delete=models.PROTECT, null=True)
    student = models.ForeignKey(Students, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.teacher.__str__() + " " + self.student.__str__()

    def get_pk(self):
        return self.pk

    class Meta:
        verbose_name = 'Связь учитель-ученик'
        verbose_name_plural = 'Связи учителя-ученики'


class Compositions(models.Model):
    name = models.CharField(verbose_name='Название произведения', max_length=100)
    author = models.CharField(verbose_name='Автор произведения', max_length=100)

    def __str__(self):
        return str(self.name) + " " + str(self.author)

    def get_pk(self):
        return self.pk

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'


class StudentComposition(models.Model):
    student = models.ForeignKey(Students, on_delete=models.PROTECT, null=True)
    comp = models.ForeignKey(Compositions, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.student.__str__() + self.comp.__str__()

    class Meta:
        verbose_name = 'Связь произведение-ученик'
        verbose_name_plural = 'Связи произведения-ученики'


