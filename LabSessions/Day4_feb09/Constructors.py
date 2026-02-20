class Book:
    def __init__(self,title,author):
        self.title = title
        self.author=author
    def display(self):
        print(self.title,self.author)
e1=Book("book1","varma")
e2=Book("book2","sharma")
e3=Book("book3","varun")

e1.display()
e2.display()
e3.display()