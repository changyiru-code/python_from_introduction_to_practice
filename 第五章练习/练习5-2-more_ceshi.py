str1 = 'sdffgg'
str2 = 'vnkvn'
print(str1 == str2)
str1 = 'sdffgg'
str2 = 'sdffgg'
print(str1 == str2)

str1 = 'BMW'
print(str1.lower() == 'bmw')
print(str1.lower() == 'Bmw')

age = 18
print(age == 18)  # 括号里的语句只是条件测试，不属于if语句
print(age < 18)
print(age > 18)
print(age <= 18)
print(age >= 18)
print(age != 18)

age1 = 18
age2 = 23
print(age1>22 and age2>22)
age1 = 26
age2 = 23
print(age1>22 and age2>22)

age1 = 18
age2 = 23
print(age1>22 or age2>22)

age1 = 18
age2 = 20
print(age1>22 and age2>22)

foods = ['apple', 'banana', 'orange', 'pie', 'strawbary']
print('apple' in foods)
print('watermelon' in foods)

foods = ('apple', 'banana', 'orange', 'pie', 'strawbary')
print('apple' not in foods)
print('watermelon' not in foods)

