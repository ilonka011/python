import random

# checking the 'type' command
print(type('Leondardo da Vinci'))
print(type([223, 14, 23, 20, 99999]))
print(type(True))

# checking the 'range' command
for i in range(1, 7):
    print(i)
for n in range(8, 29):
    print(n)
# checking the 'round'' command
print(round(23.76890013))
print(round(126.1112))

# cheking the 'input' command
input('What is the weather like? ')
input('What is your age (in years) ?')

#checking the 'len' command
love = 'I love him a lot'
print(len(love))

list1 = [11, 23, 99, 20, 97, 87]
print(len(list1))

fruit = ['banana', 'jaca', 'maracuja', 'pitomba', 'jambo', 'cherry']
print(random.choose(fruit))
print('Eat some more!!!')
print(random.choose(fruit))

never_mind = 'Sorry for saying that'
print(len(never_mind))
print(len(love))
