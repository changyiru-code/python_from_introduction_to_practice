counts = {
    'a': [3,4,5],
    'b': [4,5,6],
    'c': [5,7,8],
    'd': [6,2,1],
    'e': [7,4,2],
          }
print(f"a's favorite number is:", ','.join(list(map(lambda x:str(x),counts['a']))))
print(f"b's favorite number is {counts['b']}")
print(f"c's favorite number is {counts['c']}")
print(f"d's favorite number is {counts['d']}")
print(f"e's favorite number is {counts['e']}")

"""
list转str:
如果列表中的元素有int型，必须先把int转成str,然后在做字符串拼接

lst = [1, 2, 3]

将所有的int转换为str

lst1=list(map(lambda x:str(x),lst))

str1= ''.join(lst)

列表中的所有元素都是字符串

lst = ['a', 'b', 'c', 'd', 'e', 'f','123']

str1 = ''.join(lst)
"""
counts = {
    'a': 3,
    'b': 4,
    'c': 5,
    'd': 6,
    'e': 7,
          }
print("a, which number is your favorite?")
print(f"My favorite number is {counts['a']}")
print("b, which number is your favorite?")
print(f"My favorite number is {counts['b']}")
print("c, which number is your favorite?")
print(f"My favorite number is {counts['c']}")
print("d, which number is your favorite?")
print(f"My favorite number is {counts['d']}")
print("e, which number is your favorite?")
print(f"My favorite number is {counts['e']}")

for count, number in counts.items():
    print('\n'+count.title()+"'s favorite number is " +str(number))