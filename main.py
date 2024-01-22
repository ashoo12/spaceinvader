import random
import time
from turtle import Turtle,Screen
# create game window
screen=Screen()
screen.setup(width=800,height=800)

# create player
player=Turtle()
player.shape("turtle")
player.setheading(90)
player.penup()
player.sety(-250)
player.speed(0)

# player movement speed
player_speed=15


# create player_bullet
player_bullet=Turtle("circle")
player_bullet.shapesize(stretch_len=0.2, stretch_wid=0.5)
player_bullet.penup()
player_bullet.speed(0)
player_bullet.hideturtle()
player_bullet.setposition(x=player_bullet .xcor(), y=-250)
# player_bullet movement speed
bullet_speed = 25
# bulllet state ready or fire
bullet_state="ready"


# create enemy
x_positions=[-90,-60,-30,0,30,60,90]
y_positions=[200,250,300]
enemies=[]
for n in range(0,7):
    for y in range(0,3):
        new_enemy=Turtle("turtle")
        new_enemy.penup()
        new_enemy.setheading(90)
        new_enemy.setposition(x=x_positions[n],y=y_positions[y])
        new_enemy.speed(0)
        enemies.append(new_enemy)

# enemy movement speeed
enemy_speed =5

# create enemy player_bullet
enemy_bullet=Turtle("circle")
enemy_bullet.shapesize(stretch_len=0.2,stretch_wid=0.5)
enemy_bullet.penup()
enemy_bullet.speed(0)
enemy_bullet.hideturtle()

# enemy_bullet interval
enemy_bullet_interval=0.2
# enemy_bullet movement speed
enemy_bullet_speed = 5

# score variable
score=0

# create scoreboard
scoreboard=Turtle()
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(x=-300,y=340)
scoreboard.write(f"score:{score}" ,font=("Courier", 24, "normal"))


#update score
def update_score():
    global score
    scoreboard.clear()
    score+=1
    scoreboard.write(f"Score:{score}",font=("Courier", 24, "normal"))

# turns of player
turns=3

# turtle for turns
player_turns=Turtle()
player_turns.hideturtle()
player_turns.penup()
player_turns.goto(x=-300,y=360)
player_turns.write(f"Turns:{turns}",font=("Courier", 24, "normal"))

# update turns
def update_turns():
    global turns
    player_turns.clear()
    turns-=1
    player_turns.write(f"Turns:{turns}",font=("Courier", 24, "normal"))

def is_collision(t1,t2):
    distance=t1.distance(t2)
    if distance<15:
        return True
    else:
        return False

def fire_bullet():
    global bullet_state
    bullet_state="fire"
    y = player_bullet.ycor()
    y += bullet_speed
    x = player.xcor()
    player_bullet.setposition(x=x, y=y)
    player_bullet.showturtle()

def enemy_bullet_movement():
    y=enemy_bullet.ycor()
    y-=enemy_bullet_speed
    x=enemy_bullet.xcor()
    enemy_bullet.setposition(x,y)
    enemy_bullet.showturtle()

def move_left():
    x=player.xcor()-player_speed
    player.setx(x)

def move_right():
    x=player.xcor()+player_speed
    player.setx(x)

# creating buttons function
screen.listen()
screen.onkey(move_left,"Left")
screen.onkey(move_right,"Right")
screen.onkey(fire_bullet,"space")

game_is_on=True
while game_is_on:

    # enemy movement
    for enemy in enemies:
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)
        # enemy collision with wall
        if enemy.xcor()>380 or enemy.xcor()<-380:
            enemy_speed*=-1

    # enemy bullet movement
    enemy_bullet_movement()
    current_time = time.time()
    if current_time % enemy_bullet_interval <= 0.1:  # A small buffer for precision
        enemy_bullet_movement()
    # player BULLET MOVEMENT
    if bullet_state=="fire":
        y = player_bullet.ycor()
        y += bullet_speed
        x = player_bullet.xcor()
        player_bullet.setposition(x=x, y=y)
        player_bullet.showturtle()

    # player_bullet collision with wall
    if player_bullet.ycor()>380:
       bullet_state="ready"
       player_bullet.setposition(x=player.xcor(), y=-250)


    # enemy_bullet collision with wall
    if enemy_bullet.ycor()<-380:
        enemy_bullet.setposition(x=enemy.xcor(), y=300)

    # check for enemy and player_bullet collission
    for enemy in enemies:
        if is_collision(enemy, player_bullet):
            bullet_state="ready"
            player_bullet.hideturtle()
            enemy.hideturtle()
            update_score()
            player_bullet.setposition(x=player.xcor(), y=-250)

    # check for player and enemy_bullet collission
    if is_collision(player, enemy_bullet):
        player.hideturtle()
        update_turns()
        enemy_bullet.setposition(x=enemy.xcor(), y=300)
        player.showturtle()
    if turns<=0:
        player.hideturtle()
        player_turns.clear()
        for enemy in enemies:
            enemy.hideturtle()
        enemy_bullet.hideturtle()
        player.hideturtle()
        player_bullet.hideturtle()
        player_turns.goto(x=0,y=0)
        player_turns.write("GAME OVER",font=("Courier", 24, "normal"))
        game_is_on=False

    screen.update()




screen.exitonclick()