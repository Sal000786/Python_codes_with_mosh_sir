# class salman():
#     def __init__(self,name) :
#         self.name=name
#         print(name)
#     def talk(self):
#         print("person is talking")
# x=salman("farid ali")
# print(x.name)
# x.talk()



class salman():
    def __init__(self,name) :
        self.name=name
    def talk(self):
        print(f'Hii, {self.name} is talking')
x=salman("farid ali")
x.talk()

y=salman("salman faizi")
y.talk()