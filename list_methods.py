from typing import Reversible
from django.urls import clear_script_prefix


list=[10,20,30,40,50]
list.append(100)
print(list)

list.insert(0,200)
print(list)

list.remove(200)
print(list)

# list.clear()
# print(list)

print(list)

list.pop()
print(list)

print(list.index(50))
print(50 in list)

print(list.count(50))

list.sort()
print(list)

list.sort(reverse=True)


print(list)

list.reverse()
print("reversed list=",list)
list.reverse()
print("reversed list=",list)

copylist=list.copy()
copylist.append('salman')

print(list)
print(copylist)
 


sal=[1,10,20,30,1]
# dup=[0]
# for item in sal:
#     if item==dup:
#         x=sal.remove(item)
#         print(x)
#     else:
#         print('x')


#program to sort the repeated item in a list   
sal2=[]
for i in sal:
    if i not in  sal2:
        sal2.append(i)
        print(sal2)
# print(sal)
    