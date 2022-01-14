from parent import Fruit

class Mango(Fruit):
    
    def set_variety(self, v):
        self.variety = v
    
    def detail(self):
        self.show()
        print("Variety:", self.variety)


class Melon(Fruit):
    pass

if __name__ == "__main__":
    m1 = Mango('mango','large','oval',color='yellow')
    m1.set_variety('alphonso')
    m2 = Mango('mango','medium','oval',color='yellow')
    m2.set_variety("dassheri")
    m1.detail()
    m2.detail()
    m3 = Melon("Muskmelon",'medium','sphere','crap','wheatish')

