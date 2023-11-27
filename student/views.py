from datetime import datetime

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, \
    PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.views.generic import DetailView

from student.filters import StudentFilter
from student.forms import StudentForm, StudentUpdateForm
from student.models import Student, HistoryStudent


# CreateView -> folosit pentru a genera un formular pe baza modelului si pentru a salva datele in baza de date
# SuccessMessageMixin este o clasa in Django folosita pentru a afisa mesaje de success catre utilizator dupa ce au efectuat anumite actiuni
class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin,
                        SuccessMessageMixin, CreateView):
    template_name = 'student/create_student.html'
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy(
        'list-of-students')  # dupa salvarea datelor in tabela specificam unde sa fie redirectionat utilizatorul.
    success_message = 'Studentul {fname} {lname} a fost adaugat cu succes. Adresa lui de email este: {email}.'
    permission_required = 'student.add_student'

    def get_success_message(self, clened_data):
        return self.success_message.format(fname=self.object.first_name,
                                           lname=self.object.last_name,
                                           email=self.object.email)

    def form_valid(self, form):
        if form.is_valid():
            new_student = form.save(commit=False)
            new_student.first_name = new_student.first_name.title()
            new_student.save()
            history_text = f'{new_student.first_name} {new_student.last_name} was successfully created on {datetime.now()}'
            HistoryStudent.objects.create(message=history_text,
                                          created_at=datetime.now(),
                                          active=True, user=self.request.user)

        return redirect('list-of-students')


# ListView ->   este o clasa generica in Django folosita pentru a afisa o lista de obiecte dintr-un model intr-o pagina web

class StudentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'student/list_of_students.html'
    model = Student
    context_object_name = 'all_students'
    permission_required = 'student.view_list_of_students'

    #     variabila de sus context reprez toate datele din tabela students-students

    def get_queryset(self):
        # este o metoda utilizata in clasele de view pentru a obtine si returna setul de obiecte care va fi folosit pentru afisare
        return Student.objects.filter(active=True)

    # Atunci cand folositi o clasa bazata pe view in Django, pe baza acestei metode va permite sa adaugati variabile suplimentare la context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = datetime.now()  # in variabila now stochez data si ora curenta
        context['current_datetime'] = now

        students = Student.objects.filter(
            active=True)  # stocam in variabila students,studentii care vin in interfata, adica cei care au active=True
        filters = StudentFilter(self.request.GET,
                                queryset=students)  # in urma valorilor completate in inputurile din formularul de filtrare vor ramane
        # studentii care respecta conditiile din filtrare
        students = filters.qs  # in varibiala students reinitializam variabila, din cei toti active=True raman doar cei care vin in urma filtarii.
        context[
            'all_students'] = students  # trimitem in interfata pe baza cheii all_students toti studenti ramasi in urma filtrariii
        context[
            'form_filters'] = filters.form  # trimitem in interfata formularul de filtare

        return context


# UpdateView-> este o clasa generica in Django folosita pentru a actualiza un obiect salvat in baza de date

class StudentUpdateView(LoginRequiredMixin, PermissionRequiredMixin,
                        UpdateView):
    template_name = 'student/update_student.html'
    model = Student
    form_class = StudentUpdateForm
    success_url = reverse_lazy('list-of-students')
    permission_required = 'student.change_student'


# DeleteView -> este o clasa generica in django  utilizata pentru a sterge un obiect din baza de date

class StudentDeleteView(LoginRequiredMixin, PermissionRequiredMixin,
                        DeleteView):
    template_name = 'student/delete_student.html'
    model = Student
    success_url = reverse_lazy('list-of-students')
    permission_required = 'student.delete_student'


# DetailView -> este o clasa generica in django utilizata pentru a afisa detalii despre un obiect dintr-un model din baza de date

class StudentDetailView(LoginRequiredMixin, PermissionRequiredMixin,
                        DetailView):
    template_name = 'student/details_student.html'
    model = Student
    permission_required = 'student.view_student'


@login_required
# @permission_required('app_label.codename')
@permission_required('student.delete_student')
def delete_student_modal(request, pk):
    Student.objects.filter(id=pk).delete()

    return redirect('list-of-students')
