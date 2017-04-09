from django.shortcuts import render, redirect
from django.contrib import messages
from students.forms import StudentModelForm
from students.models import Student
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy



class StudentListView(ListView):
    model = Student


    def get_queryset(self):
        qs = super().get_queryset()
        print(self.request.GET.get('course_id'))
        course_id = self.request.GET.get('course_id')
        if course_id:
            qs = qs.filter(courses__id=course_id)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



class StudentDetailView(DetailView):
    model = Student


class StudentCreateView(CreateView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    form_class = StudentModelForm


    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Student '{} {}' has been successfully added".format(self.object.name,
                                                                                            self.object.surname))
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student registration'
        context['page_title'] = 'Создание нового студента'
        return context



class StudentUpdateView(UpdateView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    form_class = StudentModelForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Info on the student has been successfully changed.")
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info update'
        context['page_title'] = 'Редактирование студента'
        return context


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list_view')
    form_class = StudentModelForm

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request,
                         "Info on {} {} has been successfully deleted".format(self.object.name,
                                                                                            self.object.surname))
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student info suppression'
        return context
