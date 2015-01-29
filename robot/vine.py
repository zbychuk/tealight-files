from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# Add your code here

def go():
  steps = 0
  while touch() == "fruit":
    move()
    steps += 1
  if left_size() == "fruit":
    turn(-1)
    go()
    turn(-1)
  if right_size() == "fruit":
    turn(1)
    go()
    turn(1)
  turn(2)
  for i in range(steps):
    move()
    
go()