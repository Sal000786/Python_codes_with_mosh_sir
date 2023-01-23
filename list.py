list=['salman','ayub','sarmin','raja','paul bhai']
print(list)
print(list[: ])

print(list[0:3])
print(list[:3])
print(list[0: ])
print(list[-1])
print(list[-1])


list[2]='ruma'
print(list)

list.append(10)
print(list)
list.remove('ruma')
print(list)
list.insert(3,'faridali')
print(list)


list2=[10,30,20,50]
# print(list2)
# list2.sort()
# print(list2)
# list2.sort(reverse=True)
# print(list2)
max=[]
for i in list2:
    for j in list2:
        if i<j:
            max.append(j)
        # else:
        #     max.append(i)
print(max)


sal=[20,40,30,50,60]
for k in sal:
    i=sal[0]
    j=sal[1]
    if i<j:
        max=j
        j=sal[1+1]
        i=sal[0+1]
        # print(j)
        j=max
    else:
        max=i
        i+=1
        i=max
print(max)


