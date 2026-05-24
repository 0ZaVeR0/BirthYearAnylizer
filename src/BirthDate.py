import datetime

class BirthDate:
    def __init__(self, day = 1, month = 1, year = 2000) -> None:
        self.setDateFromInts(day, month, year)
    
    def setDateFromInts(self, newDay: int, newMonth: int, newYear: int) -> None:
        self.checkValidDate(newDay, newMonth, newYear)
        self.day = newDay
        self.month = newMonth
        self.year = newYear

    def setDateFromStr(self, newDate, sep=" "):
        try: 
            day, month, year = [int(x) for x in newDate.strip().split(sep)]
        except ValueError:
            raise ValueError("Не int")
        self.setDateFromInts(day, month, year)

    def checkValidDate(self, day: int, month: int, year: int) -> None:
        daysInMonth = [0, 31, 29, 31, 30, 31 ,30, 31, 31, 30, 31, 30, 31]

        if year < 1: 
            raise ValueError(f'Год не может быть < 1. Год: {year}')
        if month > 12 or month < 1: 
            raise ValueError(f'Месяц не может быть > 12 или < 1. Месяц: {month}')
        if day < 1 or day > daysInMonth[month]: 
            raise ValueError(f'День выходит за границы допустимого значения. День: {day}')

        if month == 3 and not self.isLeepYear(year) and day > 28: 
            raise ValueError(f'День выходит за границы допустимого значения. День: {day}')

    def isLeepYear(self, year: int) -> bool:
        if year % 4 == 0:
            if year % 100 == 0:
                return year % 400 == 0
            return True
        return False
    
    def getDayOfWeek(self):
        weekdays = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
        date = datetime.date(self.year, self.month, self.day)
        return weekdays[date.weekday()]

    def getAge(self) -> int:
        today = datetime.date.today()
        age = today.year - self.year
        if (today.month, today.day) < (self.month, self.day):
            age -= 1
        return age if age >= 0 else -1
    
    def checkLeapYear(self) -> bool:
        return self.isLeepYear(self.year)

