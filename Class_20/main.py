# lambda function


"""
Normal Function
def function(Parameters):

->lambda fucntion
    ->Anonymous Function/Unnamed Function
    ->lambda keyword
    ->Single statemeny
"""
# lst=5
# add=lambda num: num+lst
# print(add(5))
#
#


# filter(function,iterable)
#
# lst=[12,34,55,61,74,43]
# def odd_function(num):
#     return num%2 !=0
# odd=filter(odd_function,lst)
# print(list(odd))
#
#
# lst=[12,34,55,61,74,43]
# even=filter(lambda num: num%2==0,lst)
# print(list(even))


# map (function,iterable)


#
# lst=[1,2,3,5,6,7]
# sqr=map(lambda value: value**2,lst)
# print(list(sqr))
#


l=[1,2,3,4,5,6,7,8,9,10,11]
even_odd=map(lambda num: num+5 if num%2==0 else num+2,l)
print(list(even_odd))










