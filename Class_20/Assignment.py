
# Write a python program to count even and odd in a list of Integers using lambda function.

lst=[]
end=int(input("How many number do you want: "))

for item in range (end):
    num=int(input("Enter any number: "))
    lst.append(num)
print(lst)

even=len(list(filter(lambda num: num%2==0,lst)))
odd=len(list(filter(lambda num: num%2!=0,lst)))

print(even)
print(odd)