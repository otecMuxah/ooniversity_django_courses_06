from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from courses.forms import CourseModelForm, LessonModelForm
from courses.models import Course, Lesson
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course'
    template_name = 'courses/detail.html'

    def get_queryset(self):
        qs = super().get_queryset()
        course_id = self.request.GET.get('course_id', None)
        if course_id:
            qs = qs.filter(courses__id=course_id)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lessons_list'] = Lesson.objects.filter(course=self.object.pk)
        context['course'] = Course.objects.get(id=self.object.pk)
        return context


class CourseCreateView(CreateView):
    model = Course
    form_class = CourseModelForm
    success_url = reverse_lazy('index')
    context_object_name = 'course'
    template_name = 'courses/add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course creation'
        # context['button_name'] = 'Add'
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Course {} has been successfully added.'.format(self.object.name))
        return response


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CourseModelForm
    context_object_name = 'course'
    template_name = 'courses/edit.html'

    def get_success_url(self):
        return reverse('courses:edit', args=(self.object.pk,))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course update'
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'The changes have been saved.')
        return response


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy('index')
    context_object_name = 'course'
    template_name = 'courses/remove.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course deletion'
        return context

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, 'Course {} has been deleted.'.format(self.object.name))
        return response

class LessonCreateView(CreateView):
    model = Lesson
    template_name = 'courses/add_lesson.html'
    form_class = LessonModelForm
    context_object_name = 'lessons'
    success_url = reverse_lazy('courses:detail')

    def get_initial(self):
        initial = super().get_initial()
        course = Course.objects.get(id=self.kwargs['pk'])
        initial['course'] = course
        return initial

    def get_success_url(self, **kwargs):
        return reverse_lazy('courses:detail', args=(self.kwargs['pk']))

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Lesson has been successfully added.")
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "ADD LESSON"
        return context

                # def detail(request, course_id):
#     course = Course.objects.get(id=course_id)
#     lessons_list = Lesson.objects.filter(course=course)
#
#
#     context = {
#         'course': course,
#         'lessons_list': lessons_list
#
#     }
#     return render(request, 'courses/detail.html', context)
#
#
# @csrf_exempt
# def add(request):
#     context = {}
#     if request.method == "POST":
#         form = CourseModelForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             form.save()
#             message = 'Course {} has been successfully added.'.format(data['name'])
#             messages.success(request, message)
#             return redirect('/')
#     else:
#         form = CourseModelForm()
#
#     context['form'] = form
#
#     return render(request, 'courses/add.html', context)
#
#
# @csrf_exempt
# def edit(request, course_id):
#     context = {}
#     course = Course.objects.get(id=course_id)
#
#     if request.method == 'POST':
#         form = CourseModelForm(request.POST, instance=course)
#         if form.is_valid():
#             form.save()
#             message = 'The changes have been saved.'
#             messages.success(request, message)
#             return redirect('courses:edit', course_id=course_id)
#     else:
#         form = CourseModelForm(instance=course)
#
#     context['form'] = form
#
#     return render(request, 'courses/edit.html', context)
#
#
# @csrf_exempt
# def remove(request, course_id):
#     context = {}
#     course = Course.objects.get(id=course_id)
#     if request.method == 'POST':
#         course.delete()
#         message = 'Course {} has been deleted.'.format(course.name)
#         messages.success(request, message)
#         return redirect('/')
#     context['course'] = course
#
#     return render(request, 'courses/remove.html', context)
#
# @csrf_exempt
# def add_lesson(request, course_id):
#     context = {}
#     course = Course.objects.get(id=course_id)
#     if request.method == "POST":
#         form = LessonModelForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             form.save()
#             message = 'Lesson {} has been successfully added.'.format(data['subject'])
#             messages.success(request, message)
#             return redirect('courses:detail', course_id)
#     else:
#         form = LessonModelForm(initial={'course': course})
#
#     context['form'] = form
#
#     return render(request, 'courses/add_lesson.html', context)