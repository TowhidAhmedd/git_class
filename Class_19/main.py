#Exam -01

# lst=[1,2,3,4,5]
#
# sum=0
# def count(n):
#     global sum
#     for i in n:
#         sum+=i
#     return sum
# print(count(lst))


# Exam-02




def get(lst):
    l=[]
    for i in lst:
        if i in l:
            l.append(i)
    return lst

original=[1,2,2,3,3,4,5]
print(get(original))













