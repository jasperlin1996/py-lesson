import decimal
a = input()
b = input()
c = input()
d = decimal.Decimal(a) * ((decimal.Decimal(b))**decimal.Decimal(c))
print(d)
print(type(d))