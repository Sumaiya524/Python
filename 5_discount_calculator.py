# -*- coding: utf-8 -*-
"""5.discount calculator

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1C0Accb99ZiYmSbsHbaORVsA0wm8quV6o
"""

amount = float(input("Enter the purchase amount: $"))
if amount > 100:
  discount = 0.10
else:
  discount = 0.05
discounted_amount = amount - (amount * discount)
print(f"Original price: ${amount:.2f}")
print(f"Discount applied: {discount * 100}%")
print(f"The discounted amount is ${discounted_amount:.2f}")