a = ('a' , 'b' , 'c' , 'd')

b = list(a)
print(b)

b[0] = 'u'

a = tuple(b)
print(a)