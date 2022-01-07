class Person:

    age = 12

    def greet(self):
        print("Hello!")


if __name__ == "__main__":
    alex = Person() # create a object of named alex using class Person
    alex.greet()
    print("old age",alex.age)
    alex.age = 25 # we can change the property value 
    print("new age",alex.age)

    hari = Person()
    hari.greet()
    print(hari.age)