class Fruit:
    def __init__(self,name,price):
        self.name = name
        self.price =price

    def display(self):
        print("name:%\n,price:%p",(self.name,self.price))

fruit1 = Fruit("Bananas",10)
fruit2 = Fruit("Mangoes",10)
fruit3 = Fruit("Oranges",10)
fruit4 = Fruit("Pears",20)
fruit5 = Fruit("Apples",30)
fruit6 = Fruit("avacadoes",30)


fruit1.display()
fruit2.display()
fruit3.display()
fruit4.display()
fruit5.display()
fruit6.display()



