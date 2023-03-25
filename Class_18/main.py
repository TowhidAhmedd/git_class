

num=int(input("Enter: "))

# def increase(n):
#     if n==0:
#         return
#
#     elif n%2!=0:
#         increase(n-1)
#         print(n)
#
#
#
# increase(10)


# def towhid(n):
#     if n==0:
#         return n
#     else:
#         return n+towhid(n-1)
#
#
# print(towhid(num))

def towhid(n):
    if n==0:
        return 0
    else:
        return n+towhid(n-1)


print(towhid(num))














