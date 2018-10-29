# python lesson hw02-1
# 2018/10/22

n = int(input("input n: "))

for i in range(n):
    year = int(input())
    if ((year%4==0 and year%100!=0 ) or (year%400 ==0)):
        print("{} is a leap year!".format(year))
    else:
        print("{} is a common year.".format(year))