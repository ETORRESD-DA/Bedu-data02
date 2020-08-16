import random
number = input('Give me a number: ')
index = random.randint(1, int(number))
counter = 1
list_random = []
while counter <= index:
    choice = random.randint(1, 2)
    if choice == 1:
        value = str(counter)
    else:
        value = int(counter)
    list_random.append(value)
    counter = counter + 1
print(list_random)
