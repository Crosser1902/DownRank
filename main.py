import pynput
from pynput import mouse, keyboard
from pynput.mouse import Button, Controller
import  time

start = {"mainscreen":(327,256),"leftscreen":(-906,209)}
jump = {"mainscreen":(-787,380),"leftscreen":(-787,380)}
Esc = {"mainscreen":(2109,194),"leftscreen":(-202,194)}
exit = {"mainscreen":(320,1249),"leftscreen":(-891,591)}
yes = {"mainscreen":(1475,981),"leftscreen":(-500,506)}
Home = {"mainscreen":(1475,981),"leftscreen":(-20,700)}


currentscreen = "leftscreen"
mouse = Controller()


for i in range(60):
    print(i+1)
    mouse.position = start[currentscreen]
    mouse.click(Button.left, 1)
    print("start")

    time.sleep(95)

    mouse.position = jump[currentscreen]
    mouse.click(Button.left, 1)
    print("jump")

    time.sleep(2)

    mouse.position = Esc[currentscreen]
    mouse.click(Button.left, 1)
    print("Esc")

    time.sleep(3)

    mouse.position = exit[currentscreen]
    mouse.click(Button.left, 1)
    print("exit")

    time.sleep(3)

    mouse.position = yes[currentscreen]
    mouse.click(Button.left, 1)
    print("yes")

    time.sleep(35)

mouse.position = Home[currentscreen]
mouse.click(Button.left, 1)
print("Home")
