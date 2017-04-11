
from django.contrib import messages
from courses.forms import CourseModelForm, LessonModelForm
from courses.models import Course, Lesson
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Course creation'
        lessons = Lesson.objects.filter(course=self.kwargs['pk'])
        context['lessons_list'] = lessons
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
        return reverse_lazy('courses:edit', args=(self.object.pk,))

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
