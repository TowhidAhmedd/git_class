

#

st=1
end=5

sum=0
sum2=0
while st<end:
    num=int(input("Enter number: "))
    if num%2==0:
        sum+=num
    else:
        sum2+=num
        st+=1

print("Even number is:",sum)
print("Odd number is:",sum2)

if sum>sum2:
    print("Even is winner")
elif sum<sum2:
    print("Odd is winner")
else:
    print("Even and Odd are equal")








# start=int(input("Enter first number"))
# end=int(input("Enter second number: "))
#
# sum=0
# sum2=0
# while start<=end:
#     num=int(input("Enter any number: "))
#     num+=sum
#     sum+=num
# print("Total sum is: ",sum)
#




# start=int(input("Enter first number"))
# end=int(input("Enter second number: "))
#
# sum=0
# sum2=0
#
# while end>=start:
#     num=int(input("Enter: "))
#     sum=sum+num
#     start=start+1
#     print(sum)








