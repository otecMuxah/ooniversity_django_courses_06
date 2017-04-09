from django.urls import reverse_lazy
from django.views.generic import CreateView
from feedbacks.models import Feedback
from feedbacks.forms import FeedbackModelForm
from django.core.mail import mail_admins
from django.contrib import messages

# Create your views here.
class FeedbackView(CreateView):
    template_name = 'feedback.html'
    model = Feedback
    form_class = FeedbackModelForm
    success_url = reverse_lazy('feedback')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Thank you for your feedback! We will keep in touch with you very soon!')
        mail_admins(self.object.subject, self.object.message, self.object.from_email)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Feedback'
        context['page_title'] = 'Send your feedback'
        return context
