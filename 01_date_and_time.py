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
