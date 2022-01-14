
class ListX(list):
    
    def sum(self):
        return sum(self)

    def mean(self):
        return sum(self)/len(self)

    def max(self):
        return max(self)

x = ListX() # empty list
for i in range(10):
    x.append(int(input(">> value >>")))

print(x.sum())
print(x.mean())
print(x.max())