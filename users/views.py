from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from .forms import RegisterUserForm, LoginUserForm
from .models import Students, Teachers, TeacherStudent


def personalisation(request):
    st = Students.objects.all()
    tc = Teachers.objects.all()
    ts = TeacherStudent.objects.all()
    data1 = []
    data2 = []
    for s in st:
        if s.user == request.user:
            data1.append(s)
            for i in ts:
                if s == i.student:
                    data2.append(i.teacher)
    for t in tc:
        if t.user == request.user:
            data2.append(t)
            for i in ts:
                if t == i.teacher:
                    data1.append(i.student)
    return render(request, 'users/personalisation.html', {'student': data1, 'teacher': data2, 'request': request})


def musical_lit(request):
    return render(request, 'users/musical_lit.html')


def composition(request):
    return render(request, 'users/composition.html')


def solfeggio(request):
    pass


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


