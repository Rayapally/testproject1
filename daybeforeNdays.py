def DayBefore(day,num):
    Before_day = (day-num) % 7
    print(Before_day)

day = int(input("Enter the day :"))

num = int(input("Enter the number:"))
DayBefore(day,num)
