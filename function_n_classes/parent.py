class Fruit:

    def __init__(self,name,size,shape,flavour='sweet',color='red'):
        self.size = size 
        self.shape =  shape
        self.flavour = flavour
        self.color = color
        self.name = name

    def show(self):
        print('Name:',self.name)
        print('Shape:',self.shape)
        print('Color:',self.color)
        print('Size:',self.size)
        print('Flavour:',self.flavour)

if __name__ == "__main__":
    a1 = Fruit('apple','small','pear-shaped')
    a2 = Fruit('orange','small','round',color='orange')
    a1.show()
    a2.show()
