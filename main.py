import os
import matplotlib.pyplot as plt
import numpy as np
import time as t
import math as m
import random as r
import difflib

version = "Callculator 0.2"

# GRAPHING CALC INITIATE
view_size = 10


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
    print(r"          _    _     _               _       _             ")
    print(r"   ___   / \  | |   | |    ___ _   _| | __ _| |_ ___  _ __ ")
    print(r"  / __| / _ \ | |   | |   / __| | | | |/ _` | __/ _ \| '__|   | " + version)
    print(" | (__ / ___ \| |___| |__| (__| |_| | | (_| | || (_) | |      | \x1B[3mDeveloped by Yifei & Yiran\x1B[0m")
    print(r"  \___/_/   \_\_____|_____\___|\__,_|_|\__,_|\__\___/|_| ")
    print()
    print("\033[1m  | " + path + "\033[0m")

def custom_logo(title, desc):
    clear()
    
    print(r"          _    _     _               _       _             ")
    print(r"   ___   / \  | |   | |    ___ _   _| | __ _| |_ ___  _ __ ")
    print("  / __| / _ \ | |   | |   / __| | | | |/ _` | __/ _ \| '__|     \033[1m" + title + "\033[0m")
    print(" | (__ / ___ \| |___| |__| (__| |_| | | (_| | || (_) | |        \x1B[3m" +  desc + "\x1B[0m")
    print(r"  \___/_/   \_\_____|_____\___|\__,_|_|\__,_|\__\___/|_|   ")

    random_stuff = ["!", "@", "#", "$", "%", "&", "{", "}"]

    t.sleep(2)
    
    for i in range(max(len(title), len(desc))):
        clear()

        temp_title = title[:-i-2] + r.choice(random_stuff)
        temp_desc = desc[:-i-2] + r.choice(random_stuff)
        print(r"          _    _     _               _       _             ")
        print(r"   ___   / \  | |   | |    ___ _   _| | __ _| |_ ___  _ __ ")
        print("  / __| / _ \ | |   | |   / __| | | | |/ _` | __/ _ \| '__|    " + " "* i + " \033[1m" + temp_title + "\033[0m")
        print(" | (__ / ___ \| |___| |__| (__| |_| | | (_| | || (_) | |       " + " "* i + " \x1B[3m" +  temp_desc + "\x1B[0m")
        print(r"  \___/_/   \_\_____|_____\___|\__,_|_|\__,_|\__\___/|_|")
        t.sleep(0.075)



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

def cir(radius):
    for y in range(-radius, radius + 1):
        line = ""
        for x in range(-2 * radius, 2 * radius + 1):
            dist = m.sqrt((x / 2)**2 + y**2)
            if abs(dist - radius) < 0.5:
                line += "*"
            else:
                line += " "
        print(line)

def bal():
    clear()
    logo("Callculator > Utils > bal")
    print()
    for p in range(100):
        print(" ")
    clear()
    dis = 6
    
    f = True
    #wasdwasd = True
    i = 0
    limit = 5
    while True: 
        for k in range(50):
            print()
        cir(3)
        for y in range(1,dis):
            print()
            # print(l[i])
            # print(i)
        if(f and not limit == 0):
            dis += 1
        elif(not f):
            dis -= 1
        if(dis >= limit):
            f = False
        if(dis <= 0):
            f = True
            limit = m.floor(limit*0.9)
            # //print(limit)
        print("-------------------------")
        t.sleep(0.1)
        clear()
        i+=1




def graphing_calculator():
    clear()
    logo("Callculator > Math > Graphing Calculator")
    print()
    print("\033[1m  Key Guide\033[0m")
    print("  | Use ^ for exponents")
    print("  | Use * for multiplication")
    print("  | Use x as the independent variable")
    print("  | Use /input to manually input values")
    print("  | Use /list to view list instead")
    print("  | Use /view to change view size")
    print()
    print("\033[1m  Current Settings\033[0m")
    print("  | View Size: " + str(view_size))
    print()
    print("  Please enter an equation")
    raw_equation = input("  >>> ")

    # PREFORMAT
    raw_equation = raw_equation.replace("^", "**")
    print(raw_equation)

    VALUES = []
    global a
    a = -view_size

    while a <= view_size:
        # EVALUATE
        # Replace x with value to evaluate
        raw_equation = raw_equation.replace("x", str(a))
        print(raw_equation)
        print(raw_equation.replace("x", str(a)))
        asd = eval(raw_equation)
        VALUES.append(sda)
        a+=1
        print(a)
        
    print(VALUES)

    
    # LOOP VALUES
    

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
        


def credit():
    custom_logo("| Developers", "| Yifei & Yiran")
    custom_logo("| Class", "| Computational Physics")
    custom_logo("| Instructor", "| Mrs. Rajapakse")
    custom_logo("| Made Possible By", "| Replit, Python")
    custom_logo("| Visual Graphing From", "| Matplotlib")
    custom_logo("| Math Tools From", "| Math & Random Library")
    custom_logo("| Biggest Thanks To", "| You, for checking this out!")
    home()

def home():
    clear()
    logo("Callculator > Home")
    print()
    print("\033[1m  Math\033[0m")
    print("  | Graphing Calculator")
    print("  | Equation Calculator")
    print()
    print("\033[1m  Physics\033[0m")
    print("  | Physics Simulator")
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
    command = input("  >>> ")


    searchKey = ["graphing calculator", "equation calculator", "physics simulator", "unit converter", "random number generator", "bal", "about", "credits"]
    
    matches = difflib.get_close_matches(command, searchKey, cutoff=0)[0]

    
    match matches:
        case "graphing calculator":
            graphing_calculator()
        case "equation calculator":
            print("Equation Calculator")
        case "physics simulator":
            physics_simulator()
        case "unit converter":
            unit_converter()
        case "random number generator":
            print("Random Number Generator")
        case "bal":
            bal()
        case "about":
            print("About")
        case "credits":
            credit()
            
    
home()



def about():
    clear()




