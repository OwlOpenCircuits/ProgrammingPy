import random
world = "world"
print("Hello " + world + ".") 
xpos = random.randint(1, 10)
ypos = random.randint(1, 10)
zpos = random.randint(1, 2)
print(xpos, ypos, zpos)
enemy1xpos = random.randint(1, 10)
enemy1ypos = random.randint(1, 10)
enemy1zpos = random.randint(1, 2)
print(xpos - enemy1xpos)
print(ypos - enemy1ypos)
print(zpos - enemy1zpos)
