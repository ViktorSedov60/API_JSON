from rectangl import Rectangle, Square, Circle

r1 = Rectangle(3, 4)
r2 = Rectangle(12, 5)


print("r1.get_area=", r1.get_area())
print("r2.get_area=", r2.get_area())

sq1 = Square(5)
sq2 = Square(10)

print(sq1.get_area_square())
print(sq2.get_area_square())

cr1 = Circle(5)
cr2 = Circle(5)

print(cr1.get_area_circle())
print(cr2.get_area_circle())

figure = [r1, r2, sq1, sq2, cr1, cr2]
for fig in figure:
    if isinstance(fig,Square):
        print(fig.get_area_square())
    elif isinstance(fig,Circle):
        print(round(fig.get_area_circle(), 2))
    else:
        print(fig.get_area())