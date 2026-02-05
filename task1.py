from datetime import datetime


def get_days_from_today(date):
    try:
        date_object = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        difference = today - date_object
        return difference.days
    except ValueError:
        print("Невірний формат дати. Очікується 'РРРР-ММ-ДД'")
        return None


print(get_days_from_today("2021-10-09"))
print(get_days_from_today("2025-12-31"))
