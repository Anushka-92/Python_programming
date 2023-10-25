class Parent1:
    def assign_string_one(self,str1):
        self.st1=str1
    def show_string_one(self):
        return self.str1
class Parent2:
    def assign_string_two(self,str2):
        self.st2=str2
    def show_string_two(self):
        return self.str2
class child(Parent1,Parent2):        
    def assign_string_three(self,str3):
        self.str3=str3
    def show_string_three(self):
        return self.str3
my_child=child()
my_child.assign_string_one("i am string of parent 1")
my_child.assign_string_two("i am string of parent 2")
my_child.assign_string_three("i am string of parent 3")
print(my_child.show_string_one())
print(my_child.show_string_two())
print(my_child.show_string_three())