import os
import matplotlib.pyplot as plt
import numpy as np
import time as t
import math as m

# Python thingy majigy
print("Preloading...")

class coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.init_x = x
        self.init_y = y
    def reset(self):
        self.x = self.init_x
        self.y = self.init_y
        
class object:
    def __init__(self, mass, pos, size):
        self.mass = mass
        self.pos = pos
        self.size = size
        self.vel = 0.0
    def output(self):
        print("＿"*self.size)
        for i in range(self.size-1):
            print("｜" + "　"*(self.size) + "｜")
        print("｜" + "＿"*(self.size) + "｜")
    

def logo(path):
    print(r"   ____      _ _            _       _             ")
    print(r"  / ___|__ _| | | ___ _   _| | __ _| |_ ___  _ __ ")
    print(r" | |   / _` | | |/ __| | | | |/ _` | __/ _ \| '__|    | Callcuator 0.1")
    print(" | |__| (_| | | | (__| |_| | | (_| | || (_) | |       | \x1B[3mDeveloped by Yifei & Yiran\x1B[0m")
    print(r"  \____\__,_|_|_|\___|\__,_|_|\__,_|\__\___/|_|   ")
    print()
    print("\033[1m  | " + path + "\033[0m")


def clear():
    os.system('clear')
    
def loadingScreen(task, number, total):
    # Callculator
    clear()
    logo("Callculator > Loading")
    print()
    print(" > Loading " + task)

    percentage = round(number/total*100)
    progress = round(percentage/5)
    print("[" + "="*progress + " "*(20-progress) + "] " + str(percentage), "%" )
    

loadingScreen("Library Imports", 1, 10) 
# Launch home screen
# HOME SCREEN


def unit_converter():
    clear()
    logo("Callculator > Utils > Unit Converter")
    print()


def bal():
    clear()
    logo("Callculator > Utils > bal")
    print()
    

    def print_ascii_circle(radius):
        for y in range(-radius, radius + 1):
            line = ""
            for x in range(-2 * radius, 2 * radius + 1):
                dist = m.sqrt((x / 2) ** 2 + y ** 2)
                if abs(dist - radius) < 0.5:
                    line += "*"
                else:
                    line += " "
            print(line)
    clear()
    while True:
        
        t.sleep(1)
        print_ascii_circle(2)
        t.sleep(1)
        clear()
        
        print()
        print()
        print()
        print_ascii_circle(2)
        t.sleep(1)




def graphing_calculator():
    clear()
    logo("Callculator > Math > Graphing Calculator")
    print()
    print("\033[1m  Key Guide\033[0m")
    print("  | Use ^ for exponents")
    print("  | Use * for multiplication")
    print("  | Use x as the independent variable")
    print()
    print("Please enter an equation")
    raw_equation = input("  >>> ")

    fig, axs = plt.subplots(2, 2)
    plt.show()
    
def physics_simulator():
    # INITIALIZE
    clear()
    logo("Callculator > Math > Physics Simulator > Loading...")
    print("-"*100)
    for i in range(20):
        print()
    print("="*100)
    cube = object(10, coordinate(0, 20), 10)

    
    while True:
        # Header
        clear()
        logo("Callculator > Math > Physics Simulator")
        print("＿"*100)

        # DEBUG
        print(cube.pos.y)

        # CALCULATE VELOCITY
        cube.vel += 9.8*0.25
        
        # COLLISION CHECK
        if cube.pos.y <= 0:
            cube.vel = 0
            cube.pos.y = 0
        else:
            
            # MODIFY POSITION
            cube.pos = coordinate(cube.pos.x, cube.pos.y - cube.vel*0.25)
            cube.pos.y -= cube.vel*0.25

        # RENDER
        for i in range(round(20-cube.pos.y)):
            print()

        cube.output()
        for i in range(round(cube.pos.y-cube.size)):
            print()

        print("-"*100)
        t.sleep(0.25)
        
    

def home():
    clear()
    logo("Callculator > Home")
    print()
    print("\033[1m  Math\033[0m")
    print("  | Graphing Calculator")
    print("  | Equation Calculator")
    print()
    print("\033[1m  Utils\033[0m")

    print("  | Unit Converter")
    print("  | Random Number Generator")
    print("  | bal")
    print()
    print("\033[1m  Settings\033[0m")
    print("  | About")
    print("  | Exit")
    print()
    print("Enter a command: ", end="")
    command = input()
    if command == "bal":
        bal()
    elif command == "graphing":
        graphing_calculator()
    elif command == "physics":
        physics_simulator()
home()




