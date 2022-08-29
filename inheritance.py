class Parent_class:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print("Name: ",self.name)
        print("Age: ",self.age)

class Child_class(Parent_class):
    def __init__(self,name,age, city):
        super().__init__(name, age)
        self.city = city

    def show(self):
        super().show()              #
        print("City: ",self.city)
class GrandChild_class(Child_class):
        def __init__(self,name,age,city,country):
            super().__init__(name,age,city )
            self.country = country
        def show(self):
            super().show()
            print("country:", self.country)
p = Parent_class("john",24)
p.show()
c = Child_class("john",24,"new york")
c.show()
g = GrandChild_class("john",24,"new york","USA")
g.show()



