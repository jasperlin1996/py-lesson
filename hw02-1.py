# python lesson hw02-1
# 2018/10/22

while(True):
    year = int(input())
    if ((year%4==0 and year%100!=0 ) or (year%400 ==0)):
        print("{} is a leap year!".format(year))
    else:
        print("{} is a common year.".format(year))