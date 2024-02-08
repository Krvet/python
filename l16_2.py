class Cher:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s <= 0:
            print(f'Error')
        self.s - 1

    def count_moves(self, x2, y2):
        x2 -= self.x
        y2 -= self.y
        return x2 + y2
    
c = Cher(1, 1, 2)
c.go_left()
c.go_down()
print(c.count_moves(3, 3))