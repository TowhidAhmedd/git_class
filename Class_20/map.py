

# map
#
# lst=[1,2,3,4,5,6,5]
#
# s=map(lambda num: num ** 2,lst)
# print(list(s))


lst=[3,6,34,67,34,7]

sqr=map(lambda num: num + 5 if num % 2 == 0 else num+3,lst)
print(list(sqr))


















