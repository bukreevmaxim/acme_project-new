from datetime import date


def calculate_birthday_countdown(birthday: date):
    """
    Возвращает количество дней до следующего дня рождения.

    Если день рождения сегодня, то возвращает 0.
    """
    today = date.today()
    this_year_birthday = get_birthday_for_year(birthday, today.year)

    if this_year_birthday < today:
        next_birthday = get_birthday_for_year(
            birthday,
            today.year + 1,
        )
    else:
        next_birthday = this_year_birthday

    return (next_birthday - today).days


def get_birthday_for_year(birthday: date, year: int):
    """
    Возвращает дату дня рождения для указанного года.

    День рождения 29 февраля в невисокосном году отмечается 1 марта.
    """
    try:
        return birthday.replace(year=year)
    except ValueError:
        return date(year=year, month=3, day=1)
