def checkValidDate(inputDate):
    if len(inputDate) != 3: return (1, "неверный формат")
    if len(inputDate[0]) > 2: return (2, "неверный формат")
    if len(inputDate[1]) > 2: return (3, "неверный формат")
    if len(inputDate[2]) != 4: return (4, "неверный формат")

    try:
        day = int(inputDate[0])
        month = int(inputDate[1])
        year = int(inputDate[2])
    except ValueError:
        return (5, "неверный формат")
    
    daysInMonth = [0, 31, 29, 31, 30, 31 ,30, 31, 31, 30, 31, 30, 31]

    if year < 1: return (6, "")
    if month > 12 or month < 1: return (7, "")
    if day < 1 or day > daysInMonth[month]: return (8, "")

    if month == 3 and not isLeepYear(year) and day > 28: return (9, "")

    return (0, "success")

def isLeepYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False
    
def main():
    print("Введите дату своего рождения для анализа в формате ДД ММ ГГГГ")
    while(True):
        rawIn = input(">>>").strip().split(" ")
        print(rawIn)
        check = checkValidDate(rawIn)
        if check[0] == 0:
            break
        print(check)
    

if __name__ == "__main__":
    main()