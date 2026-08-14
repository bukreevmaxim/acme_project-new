from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView

from .forms import BirthdayForm
from .models import Birthday
from .utils import calculate_birthday_countdown


def birthday(request, pk=None):
    """Здесь происходит отправка и редактирование"""
    if pk is not None:
        instance = get_object_or_404(Birthday, pk=pk)
    else:
        instance = None

    if request.method == "POST":
        form_data = request.POST
        form_files = request.FILES
    else:
        form_data = None
        form_files = None

    form = BirthdayForm(form_data, form_files, instance=instance)
    context = {"form": form}

    if form.is_valid():
        saved_birthday = form.save()
        context.update(
            {
                "birthday_countdown": calculate_birthday_countdown(
                    saved_birthday.birthday,
                ),
                "show_result": True,
            }
        )

    return render(request, "birthday/birthday.html", context)

def delete_birthday(request, pk):
    """"Здесь происходит удаление"""
    instance = get_object_or_404(Birthday, pk=pk)

    if request.method == 'POST':
        instance.delete()
        return redirect('birthday:list')

    form = BirthdayForm(instance=instance)
    context = {'form': form}
    return render(request, 'birthday/birthday.html', context)

# def birthday_list(request):
#     """"Здесь происходит вывод всех записей"""
#     birthdays = Birthday.objects.order_by('id')
#     paginator = Paginator(birthdays, 2)

#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     context = {'page_obj': page_obj}
#     return render(request, 'birthday/birthday_list.html', context)

class BirthdayListView(ListView):
    # Указываем модель, с которой работает CBV...
    model = Birthday
    # ...сортировку, которая будет применена при выводе списка объектов:
    ordering = 'id'
    # ...и даже настройки пагинации:
    paginate_by = 2 
