# lesson 2 
# num1_i: int = 1_357
# num1_i += 11.5
# num2_i = 2468
# num3_i = 3579
# num5_i = 1357
# letter = 'a'
# text = 'This is a sentence'
# num_f = 6.78
# flag = True
# flowers = ['rose','lilia','pion']
# print(type(num1_i))
# print(num1_i,id(num1_i))
# print(isinstance(num1_i,(int,float,complex)))
# print(num3_i is num1_i)
# print(id(num5_i))
# print(num5_i is num1_i)
# print(hash(num1_i))
# print(type(flowers))
# # print(hash(flowers))  # TypeError: unhashable type: 'list'
# n = input('Введите любой текст, я скажу его тип, адрес и хэш: ')
# print(type(n), id(n), hash(n))
# print(letter.__doc__)
# print(str.__doc__)
# print(int.__doc__)
# print()
# print(num1_i.__doc__)
# print(text.count('s'))
# print(dir())        # ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'letter', 'num1_i', 'text']
# print(dir(text))  
# print(help(str))   
# print(help())
# print(82 or 42)     # 82
# print(0 or 42)      # 42

# task
# intext = input('Type a text, I\'s say wheather it\'s a number: ')
# if intext.isdecimal():
#     print(bin(int(intext)), oct(int(intext)), hex(int(intext)))
# else:
#     print('It\'s ASCII text' if intext.isascii else 'It\'s not ASCII text')

# math
print(0.1 + 0.2)
import decimal
decimal.getcontext().prec = 17
precize_num = decimal.Decimal(0.1) + decimal.Decimal(0.2)
print(precize_num)

