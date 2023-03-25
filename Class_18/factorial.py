# '''
# # Factorial=1*2*3*4*5
#
#
# '''
#
# num=int(input("Enter any numebr: "))
#
# def towhid(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*towhid(n-1)
#
#
#
# print(towhid(num))
#
#



number=int(input("Enter any number: "))

def function(num):
    if num==1 or num==0:
        return 1
    else:
        return num*function(num-1)



print(function(number))
