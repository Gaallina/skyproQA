month = int(input('Введите номер месяца: '))


def month_to_season(month):
    if month in (12, 1, 2):
        print('зима')
    elif month in (3, 4, 5):
        print('весна')
    elif month in (6, 7, 8):
        print('лето')
    elif month in (9, 10, 11):
        print('осень')


month_to_season(month)
