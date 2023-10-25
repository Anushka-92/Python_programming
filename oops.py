class Phone:
    def make_call(self):
        print("make phone call")
    def play_game(self):
        print("Playing game")
    def set_color(self,color):
        self.color=color
    def set_cost(self,cost):
        self.cost=cost
    def show_color(self):
        return self.color
    def show_cost(self):
        return self.cost
p2=Phone()
p2.set_color("blue")
p2.set_cost(4000)
p2.show_color()
p2.show_cost()
