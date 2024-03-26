class Person:

    def __init__(self,name,age,gender):
        self.__name=name;
        self.__age=age;
        self.__gender=gender

    def introduce(self):
        print("\n",self.__name, self.__age, self.__gender);



name=input("\nEnter your name: ")
age=eval(input("\nEnter your age:   "))
gender=input("\nEnter your gender:")


check=Person(name,age,gender);
check.introduce();