def make_point(x, y):
    tmp = {"x" : x, "y" : y}
    return tmp

def make_segment(start, end):
    tmp = {"start" : start, "end" : end}
    return tmp
def midpoint_segment(line):
    tmp = {"x": (line["start"]["x"]+line["end"]["x"])/2, "y": (line["start"]["y"]+line["end"]["y"])/2}
    return tmp

p = make_point(5, 4)
q = make_point(4, 3)
l = make_segment(p, q)
print(midpoint_segment(l))
print("x : " + str(midpoint_segment(l)["x"]) + " y : " + str(midpoint_segment(l)["y"]))
