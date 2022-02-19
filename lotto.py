import random

#using a list so the numbers are changeable
lottery_numbers = []

for i in range(0,6):
    numbers = random.randint(1,50)
    lottery_numbers.append(numbers)

print("Lottery numbers: ")
print(lottery_numbers)

