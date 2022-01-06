def make_pretty(func):
    def inner(): #inner wrapper function
        print("〰" * 20)
        func()
        print("〰" * 20)
    return inner

@make_pretty
def ordinary():
    print("This is ordinary function")
ordinary()

x = {}
