# Written by *** for COMP9021
#
# Creates 3 classes, Point, Line and Parallelogram.
# A point is determined by 2 coordinates (int or float).
# A line is determined by 2 distinct points.
# A parallelogram is determined by 4 distinct lines,
# two of which have the same slope, the other two
# having the same slope too, but different to the other one.
# The Parallelogram class has a method, divides_into_two_parallelograms(),
# that determines whether a line, provided as argument, can split
# the object into two smaller parallelograms.


from collections import defaultdict


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

# Define a class to raise Line errors
class LineError(Exception):
    pass
class ParallelogramError(Exception):
    pass

class Line:
    def __init__(self, p1, p2):
        try:
            if p1.x == p2.x and p1.y == p2.y:
                raise ValueError
            self.p1 = p1
            self.p2 = p2
            if p2.x == p1.x:
                self.slope = float('inf')
                self.intersect = p1.x
            elif p2.y == p1.y:
                self.slope = 0
                self.intersect = p1.y
            else:
                self.slope = (p2.y - p1.y) / (p2.x - p1.x)
                self.intersect = p1.y - p1.x * self.slope
        except ValueError:
                raise LineError("Cannot create line")


    # Replace pass above with your code


# Define a class to raise Parallelogram errors


class Parallelogram:
    def __init__(self, line1, line2, line3, line4):
        try:
            a=[line1.slope,line2.slope,line3.slope,line4.slope]
            slope=list(set(a))
            line = [line1, line2, line3, line4]
            if len(slope) != 2 or len(line) != 4:
                raise ValueError
            self.sides = defaultdict(set)
            for l in line:
                self.sides[l.slope].add(l.intersect)
            for k1 in slope:
                if len(self.sides[k1]) != 2:
                    raise ValueError
                self.sides[k1] = sorted(self.sides[k1])
        except ValueError:
            raise ParallelogramError("Cannot create parallelogram")

    
            
    # Replace pass above with your code

    def divides_into_two_parallelograms(self, line):
        if line.slope not in self.sides:
            return False
        if self.sides[line.slope][0] < line.intersect < self.sides[line.slope][1]:
            return True
        else:
            return False
        # Replace the return statement above with your code
        
