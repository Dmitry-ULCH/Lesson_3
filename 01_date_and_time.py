from datetime import datetime, timedelta


def print_days():
    now = datetime.now()
    dates = [now - timedelta(days=1), now, now - timedelta(days=30),]
    for date in dates:
        print(date.strftime("%d.%m.%Y %H:%M"))
   

def str_2_datetime(date_string):
    date = datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")
    return date.strftime("%d.%m.%Y %H:%M:%S")


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))

# Такой вопрос: Если я сделаю функцию print_days() в следующем виде,
# допустимо ли вообще использовать ключи словаря на кириллице и в таком формате
# для вывода, скажем так, заголовков строк с целевыми данными?
# Т.е. заменяя тем самым текст в print

# def print_days():
#     now = datetime.now()
#     dates = {
#         "День назад": now - timedelta(days=1),
#         "Сейчас": now,
#         "30 дней назад": now - timedelta(days=30),
#     }
#     for key, date in dates.items():
#         print(f'{key}: {date.strftime("%d.%m.%Y %H:%M")}')