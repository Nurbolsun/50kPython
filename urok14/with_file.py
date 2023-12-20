import random

my_file = open ('my_name.txt', 'w') #1
my_file.write('Kunduz\n') 
my_file.close

my_file = open ('my_name.txt', 'r') #2
for line in my_file: 
    print(line)
my_file.close

with open('number_list.txt', 'w') as file: #3
    for number in range(1, 101):
        file.write(str(number) + '\n')
        file.close
    
numbers = open('number_list.txt', 'r') #4
for line in numbers:
    print(line)
numbers.close   

input = open('number_list.txt', 'r') #5
summ = 0
for line in input:
    num = list(map(int, line.split()))
    for nums in num:
     summ += nums
input.close
print("Сумма чисел из файла: ", summ)


with open('number_list.txt', 'a') as file: #6
    for number in range(1, 101):
        file.write(str(number) + '\n')




with open ('student.txt', 'r') as file: #7
    lines = file.read().splitlines()
key_value = {}
for line in lines:
    key, value = line.split(': ')
    key_value.update({key:value})
print(key_value)   
del key_value["Toktobekov Aidar"] 
print(key_value)


with open ('student.txt', 'a') as file: #8
    lines = file.read().splitlines()
key_value = {}
for line in lines:
    key, value = line.split(': ')
    key_value.update({key:value})
print(key_value)   
key_value["Temirov Azamat"] = 100
print(key_value)


