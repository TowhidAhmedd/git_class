

# filter(function,iterable)

# odd
# lst=[2,4,6,4,7,5]
# odd_lst=filter(lambda num: num % 2!=0,lst)
# print(list(odd_lst))
#
# # even
# l=[152,32,54,2,6,32,45,67,234,23]
# even_l=filter(lambda n: n % 2==0,l)
# print(list(even_l))


def odd(num):
    if num % 2==0:
        return num


lst=[21,4,3,344,3]
odd_filter=filter(odd,lst)
print(list(odd_filter))

def even(num):
    if num % 2 == 1:
        return num

l=[454,3434,23,45,56,34]
even_filter=filter(even,l)
print(list(even_filter))





