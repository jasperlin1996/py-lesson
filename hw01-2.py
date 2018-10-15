# python lesson hw01-2
# 2018/10/05

from decimal import Decimal as dec

money = dec(input("本金:"))
rate = dec(input("利率:"))
years = dec(input("存幾年:"))

print("和: {}".format(money*(1+rate)**years))