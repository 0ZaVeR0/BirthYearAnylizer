import datetime

class BirthDate:
    def __init__(self, day = 1, month = 1, year = 2000) -> None:
        self.setDateFromInts(day, month, year)
    
    def setDateFromInts(self, newDay: int, newMonth: int, newYear: int) -> None:
        """Sets date from set of ints. Raises ValueError if passed incorrect date"""
        self.__checkValidDate(newDay, newMonth, newYear)
        self.day = newDay
        self.month = newMonth
        self.year = newYear

    def setDateFromStr(self, newDate: str, sep=" ") -> None:
        """Sets date from string with specified separators. Raises ValueError if passed incorrect date"""
        try: 
            day, month, year = [int(x) for x in newDate.strip().split(sep)]
        except ValueError:
            raise ValueError("Неверное количество чисел")
        self.setDateFromInts(day, month, year)

    def __checkValidDate(self, day: int, month: int, year: int) -> None:
        """Checks for valid date. Raises ValueError if passed incorrect date"""
        daysInMonth = [0, 31, 29, 31, 30, 31 ,30, 31, 31, 30, 31, 30, 31]

        if year < 1: 
            raise ValueError(f'Год не может быть < 1. Год: {year}')
        if month > 12 or month < 1: 
            raise ValueError(f'Месяц не может быть > 12 или < 1. Месяц: {month}')
        if day < 1 or day > daysInMonth[month]: 
            raise ValueError(f'День выходит за границы допустимого значения. День: {day}')

        if month == 2 and not self.__isLeapYear(year) and day > 28: 
            raise ValueError(f'День выходит за границы допустимого значения. День: {day}')

    def __isLeapYear(self, year: int) -> bool:
        """Checks if given year is a leap year"""
        if year % 4 == 0:
            if year % 100 == 0:
                return year % 400 == 0
            return True
        return False
    
    def getDayOfWeek(self) -> str:
        """Returns day of week of stored date"""
        weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
        date = datetime.date(self.year, self.month, self.day)
        return weekdays[date.weekday()]

    def getAge(self) -> int:
        """Returns age of stored date"""
        today = datetime.date.today()
        age = today.year - self.year
        if (today.month, today.day) < (self.month, self.day):
            age -= 1
        return age if age >= 0 else -1
    
    def checkLeapYear(self) -> bool:
        """Returns if stored year is a leap year"""
        return self.__isLeapYear(self.year)

