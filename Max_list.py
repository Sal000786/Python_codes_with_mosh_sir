def max_fun(list):
    
    max=list[0]
    for i in list:
        if i>max:
            max=i
    # print("max of the list is:",max)
    return max
# size=int(input("Enter the list size: "))
# list=[]
# for i in range(size):
#     z=input(f'Enter the list item of {i+1} position : ')
#     list.append(z)
list=[10,20,50,30,40]
max_fun(list)