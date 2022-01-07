
class MyNewClass:
    '''this is s a boring class that i've created'''
    pass


class Person:
    '''this is a simple person class'''
    # attribute of class
    age = 12

    # method of class
    def greet(self):
        print("Hello!")

if __name__ == "__main__":
    print(Person.age)
    print(Person.greet)
    print(Person.__doc__)

# to use a class we should create object of the class
# a class can have multiple objects
