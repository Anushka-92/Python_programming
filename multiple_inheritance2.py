class parent:
    def get_name(self,name):
        self.name=name
    def show_name(self):
        returnself.name
class child(parent):
     def get_age(self,age):
        self.age=age
    def show_age(self):
        returnself.age
class grandchild(child):
     def get_gender(self,gender):
        self.gender=gender
    def show_gender(self):
        returnself.gender
gc=grandchild()
gc.get_name("Anushka")
gc.get_age(20)
gc.get_gender("male")
print(gc.show_name)
            