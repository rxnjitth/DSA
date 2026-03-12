
i1 = float(input())
i2 = float(input())
discount = int(input())

total = i1 + i2
discounted_price = total - total*(discount/100)
amount_saved = total*(discount/100)

print(total)
print(discounted_price)
print(round(amount_saved,2))