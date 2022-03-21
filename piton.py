import turtle

turtlePen = turtle.Turtle()
window = turtle.Screen()

window.bgcolor("black")


def polygon(n, size=80):
    if n > 4:
        angle = 360 / n

        for n in range(0, n):
            turtlePen.color(colors[n % 5])
            turtlePen.left(angle)
            turtlePen.forward(size)


turtlePen.speed(0)

colors = ['orange', 'cyan', 'blue', 'green', 'red']

size = 10

for i in range(0, 60):
    turtlePen.color(colors[i % 5])
    polygon(5, size)
    turtlePen.left(5)
    size += 5

window.mainloop()
