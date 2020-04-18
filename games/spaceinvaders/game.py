import turtle
import os

# global variables
borderspacer = 10
lborder = -300
rborder = 300
tborder = 800
bborder = 0
player_speed = 15
enemy_speed = 2
enemy_step = 20
bullet_speed = 20
bullet_state = "ready"  # ready: ready to fire ; fire: bullet is firing

# create background
wn = turtle.Screen()
wn.title("Space Invaders")
wn.bgcolor("#66ccff")
t = (rborder * 2) + 40
wn.setup(width=t, height=t)

# Draw border
bpen = turtle.Turtle()
bpen.speed(0)
bpen.color("white")
bpen.penup()
bpen.setposition(lborder, lborder)
bpen.pendown()
bpen.pensize(3)
for x in range(4):
    bpen.fd(rborder * 2)
    bpen.lt(90)
bpen.hideturtle()

# Create Player
player = turtle.Turtle()
player.color("brown")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, lborder + 15)
player.setheading(90)

# Create Player's Bullet
bullet = turtle.Turtle()
bullet.color("#ffff00")
bullet.shape("triangle")
bullet.penup()
bullet.shapesize(0.5, 0.5)
bullet.speed(0)
bullet.setheading(90)
bullet.hideturtle()

# Create Enemy
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("square")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

# Player moves
def move_left():
    x = player.xcor() - player_speed
    if x >= (lborder + borderspacer):
        player.setx(x)


def move_right():
    x = player.xcor() + player_speed
    if x <= (rborder - borderspacer):
        player.setx(x)


def fire_bullet():
    global bullet_state
    # Move the bullet
    if bullet_state == "ready":
        bullet_state = "fire"
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


# Create Keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

# Main game loop
while True:

    # Move enemy
    x = enemy.xcor()
    if x > (rborder - borderspacer) or x < (lborder + borderspacer):
        y = enemy.ycor() - enemy_step
        enemy.sety(y)
        enemy_speed *= -1
    x += enemy_speed
    enemy.setx(x)

    # Move the bullet
    y = bullet.ycor() + bullet_speed
    print(bullet_state, "- ", tborder - borderspacer, " - ", y)
    if y > tborder - borderspacer:
        bullet_state = "ready"
        bullet.hideturtle()
    else:
        bullet.sety(y)

wn.mainloop()



# with open(outfile, "wb") as file1:
#     for y in rows:
#         writer.writerows([y])
