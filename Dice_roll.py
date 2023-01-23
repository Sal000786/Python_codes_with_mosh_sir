import random
import secrets
list1=[1,2,3,4,5,6,7,8,9,0]
list2=[1,2,3,4,5,6,7,8,9,0]
list3=[]
class Dice():
    def Roll(self):

            #CAN BE SORT MORE

        # print("Start")
        # sal1=random.choice(list1)
        # list3.append(sal1)
        # sal2=random.choice(list2)
        # list3.append(sal2)
        # # print(list3)
        # print(tuple(list3))

        # # print(tuple(sal1))

        first_number=random.randint(1,6)
        second_number=random.randint(1,6)
        return first_number,second_number
salman=Dice()
print(salman.Roll())


        