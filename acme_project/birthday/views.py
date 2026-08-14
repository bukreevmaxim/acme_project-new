# birthday/views.py
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import BirthdayForm
from .models import Birthday
from .utils import calculate_birthday_countdown

class BirthdayMixin:
    model = Birthday
    form_class = BirthdayForm

class BirthdayListView(ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 10

class BirthdayCreateView(BirthdayMixin, CreateView):
    pass

class BirthdayUpdateView(BirthdayMixin, UpdateView):
    pass

class BirthdayDeleteView(DeleteView):
    model = Birthday
    success_url = reverse_lazy('birthday:list')


class BirthdayDetailView(DetailView):
    model = Birthday

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['birthday_countdown'] = calculate_birthday_countdown(
            self.object.birthday
        )
        return context