import math

def circle(radius):
    area = math.pi  * (radius ** 2)
    circ = (2 * math.pi) * radius
    return area,circ

a,b = circle(5)

print("Area: ", round(a,2) ,"Circumference: ", round(b,2))