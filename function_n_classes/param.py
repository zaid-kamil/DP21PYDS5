# check prime 3 accepts one parameter
def check_prime_3(n):
    for i in range(2,n):
        if n % i == 0:
            return "Non Prime"
    else:
        return "Prime"

# usage
print("15 is",check_prime_3(15))
print("17 is",check_prime_3(17))
print("131231 is",check_prime_3(131231))

# now we can use loop with function
x = [223,12,31,56,7,88,9]
for i in x:
    print(f'{i} is {check_prime_3(i)}')

# use with user input
num =int(input("Enter a number:"))
print(f"{num} : {check_prime_3(num)}")

