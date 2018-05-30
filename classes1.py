class student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def display(self):
        print("The details are : ", self.name ," ",  self.id)
s1 = student('bhaskar', 9)
s1.display()