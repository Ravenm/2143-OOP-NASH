from Line import Line
from Point import Point


class Polygon(object):
    """
    In class example.
    """
    def __init__(self, l1=Line):
        self.map = {}
        self.line = l1
        self.startline = l1

    def add_line(self, l1):
        """
        :description:
            Add a line to a dictionary of lines to create a polygon. Checks for duplicate values and for
            values being inserted backwards ie the line 2,4 - 3,6 is the same as 3,6 - 2,4 don't add it twice. Could
            add more logic if needed for better insertions.
        :param l1: is a line input by the user
        :type l1: line
        :return: none
        """
        self.line = l1  # storing user input in self.line
        if not self.map:  # if self.map is empty
            self.map[self.line.p1] = [self.line]  # self.map key = line.p1 value = line  example [(2,4)] [(2,4),(3,4)]
            self.startline = self.line  # sets self.startline to the first value in our dictionary
        elif self.line.p1 not in self.map.keys():       # if p1 is not a key already
            if self.line.p2 not in self.map.keys():     # if p2 is not a key. used to test if completing a polygon
                self.map[self.line.p1] = [self.line]    # insert line
            elif self.map[self.line.p2][0].p2 is not self.line.p1:  # if p2 is a key check that p1 is not a value of
                self.map[self.line.p1] = [self.line]                # that key. checking for duplicate values

    def is_complete(self, path=[]):
        """
        :description:
            Tests if a path from the first line put into polygon exists or not. Is_somthing should return a boolean
            value but im lazy so broke with convention. Goes over whole dictionary to find values that link together
            by searching for p2 of the key ie key 2,4 has p1 = 2,4 and p2 = 3,6 then we test if 3,6 is a key then
            later test if there is a key with a p2 value of startlines p1 shoing that the pionts all connect.
        :param path: empty list to hold values
        :return: path
        :rtype: list
        """
        if len(self.map) >= 3:
            self.line = self.startline  # set a starting point
            for x in range(len(self.map)):  # loop over whole thing
                if x == 0:  # if it is the first run through loop
                    path.append('(' + str(self.line.p1.x) + ',' + str(self.line.p1.y) + ')')    # add first point
                elif self.line.p2 in self.map.keys():   # else does the value of p2 point to a key
                    self.line = self.map[self.line.p2][0]   # move 'pointer' to next value
                    path.append('(' + str(self.line.p1.x)+',' + str(self.line.p1.y) + ')')  # add to list
                    if self.line.p2 is self.startline.p1:   # if the next value is the key for startline
                        path.append('complete')     # its complete
                else:
                    path.append('incomplete')   # if you ended up here no path to start found
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
