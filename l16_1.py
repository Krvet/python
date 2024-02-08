class Money:

    def __init__(self, mon):
        self.mon = mon

    def top_up(self, x):
        self.mon += x

    def count_1000(self):
        return self.mon // 1000

    def take_away(self, x):
        if self.mon < x:
            print(f'не достаточно денег')
        self.mon -= x
    
s = Money(1540)
s.top_up(1000)
print(s.mon)
print(s.count_1000())
s.take_away(1500)
print(s.mon)
s.take_away(1590)
