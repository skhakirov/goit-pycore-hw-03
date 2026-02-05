from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    result = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        diff = (birthday_this_year - today).days

        if 0 <= diff <= 7:
            congrat_date = birthday_this_year
            if congrat_date.weekday() == 5:  # суббота -> понеділок
                congrat_date += timedelta(days=2)
            elif congrat_date.weekday() == 6:  # неділя -> понеділок
                congrat_date += timedelta(days=1)

            result.append({
                "name": user["name"],
                "congratulation_date": congrat_date.strftime("%Y.%m.%d")
            })

    return result


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
