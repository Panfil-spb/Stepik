from decimal import Decimal

num = Decimal(input())

res = num.sqrt() + num.ln() + num.log10() + num.exp()

print(res)