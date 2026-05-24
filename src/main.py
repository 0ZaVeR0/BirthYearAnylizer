from BirthDate import BirthDate
from PrettyPrint import PrettyDatePrint

def main():
    date = BirthDate()
    print("Введите дату Вашего рождения для анализа в формате ДД ММ ГГГГ")
    while(True):
        rawIn = input(">>>")
        try:
            date.setDateFromStr(rawIn)
            break
        except ValueError as e:
            print(str(e))
    out = PrettyDatePrint("fonts/starFont.json")
    print(out.prettyDatePrint(date.day, date.month, date.year))
    print(date.getDayOfWeek())
    print(date.checkLeapYear())
    print(date.getAge())


if __name__ == "__main__":
    main()