from Line import Line
from Point import Point


class Polygon(object):

    def __init__(self, l1=Line):
        self.map = {}
        self.line = l1
        self.startline = l1

    def add_line(self, l1):
        self.line = l1
        if not self.map:
            self.map[self.line.p1] = [self.line]
            self.startline = self.line
        elif self.line.p1 not in self.map.keys():
            if self.line.p2 not in self.map.keys():
                self.map[self.line.p1] = [self.line]
            elif self.map[self.line.p2][0].p2 is not self.line.p1:
                self.map[self.line.p1] = [self.line]
        # return self.is_complete(self.line)

    def is_complete(self, path=[]):
        if len(self.map) >= 3:
            self.line = self.startline
            for x in range(len(self.map)):
                if x == 0:
                    path.append('(' + str(self.line.p1.x) + ',' + str(self.line.p1.y) + ')')
                elif self.line.p2 in self.map.keys():
                    self.line = self.map[self.line.p2][0]
                    path.append('(' + str(self.line.p1.x)+',' + str(self.line.p1.y) + ')')
                    if self.line.p2 is self.startline.p1:
                        path.append('complete')
                else:
                    path.append('incomplete')
                    return path
            return path

if __name__ == '__main__':
    boo = Point(2, 4)
    coo = Point(3, 4)
    hoo = Point(5, 4)
    zoo = Point(6, 4)
    loo = Line(coo, boo)
    foo = Line(boo, hoo)
    goo = Line(hoo, coo)
    b = Polygon()
    b.add_line(loo)
    b.add_line(foo)
    b.add_line(goo)
    print(b.is_complete())
