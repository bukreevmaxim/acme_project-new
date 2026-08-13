from django.shortcuts import get_object_or_404, render, redirect

from .forms import BirthdayForm
from .models import Birthday
from .utils import calculate_birthday_countdown


def birthday(request, pk=None):
    """Здесь происходит отправка и редактирование"""
    if pk is not None:
        instance = get_object_or_404(Birthday, pk=pk)
    else:
        instance = None

    form_data = request.POST if request.method == "POST" else None
    form = BirthdayForm(form_data, instance=instance)
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

def birthday_list(request):
    """"Здесь происходит вывод всех записей"""
    # Получаем все объекты модели Birthday из БД
    birthdays = Birthday.objects.all()
    # Передаём их в контекст шаблона
    context = {'birthdays': birthdays}
    return render(request, 'birthday/birthday_list.html', context)
