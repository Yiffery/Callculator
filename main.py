# FINAL STRETCH SCHEDULE
# Monday: Finish basic graphing calculator, begin 4 function calculator
# Tuesday: Finish 4 function calculator and advanced graphing calculator, begin Unit converter
# Wednesday: Finish unit converter, b
import os
version = "cALLculator 0.5"
os.system('clear')
print(r"          _    _     _               _       _             ")
print(r"   ___   / \  | |   | |    ___ _   _| | __ _| |_ ___  _ __ ")
print(r"  / __| / _ \ | |   | |   / __| | | | |/ _` | __/ _ \| '__|   | Loading...")
print(" | (__ / ___ \| |___| |__| (__| |_| | | (_| | || (_) | |      | \x1B[3mDeveloped by Yifei & Yiran\x1B[0m")
print(r"  \___/_/   \_\_____|_____\___|\__,_|_|\__,_|\__\___/|_| ")


import matplotlib.pyplot as plt
import numpy as np
import time as t
import math as m
import random as r
import difflib
import threading



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
    clear()
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
    # cALLculator
    clear()
    logo("cALLculator > Loading")
    print()
    print(" > Loading " + task)

    percentage = round(number/total*100)
    progress = round(percentage/5)
    print("[" + "="*progress + " "*(20-progress) + "] " + str(percentage), "%" )
    
loadingScreen("Library Imports", 1, 10) 

def unit_converter():
    clear()
    logo("cALLculator > Utils > Unit Converter")
    print()

def cir(radius,s):
    for y in range(-radius, radius + 1):
        line = ""
        for x in range(-2 * radius, 2 * radius + 1):
            dist = m.sqrt((x / 2)**2 + y**2)
            if abs(dist - radius) < 0.5:
                line += "*"
            else:
                line += " "
        print(" "*s,line)
constant = 3
ax = 5
h = 5
def bal(constant,ax,h):
    clear()
    # logo("Callculator > Utils > bal")
    print()

    clear()
    dis = h
    f = True
    #wasdwasd = True
    i = 0
    limit = h-1
    flag = True
    while flag: 
        for k in range(35):
            print()
        cir(constant,ax)
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
        if(limit == 0):
            flag = False
        print("---------------------------------------------------")
        t.sleep(0.05)
        clear()
        i+=1
    ask()
def ask():
    constant = 3
    ax = 5
    h = 5
    move = input("Movement Direction(x,y,z): ")
    if("x" in move.lower()):
        Xmove = input("Move X by how much: ")
        if Xmove.isdigit():
            
            ax += int(Xmove)
            bal(constant,ax,h)
        else:
            print("try again idiot")
            ask()
    if("y" in move.lower()):
        Ymove = input("Move Y by how much: ")
        if(Ymove.isdigit()):
            constant += int(Ymove)
            if(constant < 1):
                constant = 1        
            bal(constant,ax, h)
        else:
            print("try again idiot")
            ask()
    if("z" in move.lower()):
        Zmove = input("Move Z by how much: ")
        if Zmove.isdigit():
            h += int(Zmove)
            #limit += int(Zmove)-1
            #print(limit)
            t.sleep(1)
            bal(constant, ax,h)
        else:
            print("try again idiot")
            ask()
    else:
        print("try again idiot")
        ask()




def graphing_calculator():
    clear()
    logo("cALLculator > Math > Graphing Calculator")
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

    # Format Equation
    raw_equation = raw_equation.replace("^", "**")
    raw_equation = str(raw_equation)

    # Prepare Graph
    x = np.linspace(-view_size, view_size, 100)
    y = eval(raw_equation)

    # Render Graph
    plt.plot(x, y)
    plt.show(block=False)

    # Post Graph
    def post_graph_ui():
        logo("cALLculator > Math > Graphing Calculator")
        print()
        print("\033[1m  Graph Options\033[0m")
        print("  | /add + equation to add to the graph")
        print("  | /restart to restart graphing")
        print("  | /view to change the view size")
        print("  | Enter anything else to exit")
        print()

        command = input("  >>> ")
        if command.startswith("/add"):
            command = command.replace("/add", "")
            command = command.replace("^", "**")
            
            plt.plot(x, eval(command))
            plt.show()
            post_graph_ui()
        elif command.startswith("/restart"):
            graphing_calculator()
        elif command.startswith("/view"):
            global view_size
            command = command.replace("/view", "")
            view_size = int(command)
            
        else:
            home()

            # THE CALLCULATOR MUSEUM (DO NOT TOUCH BELOW):
            # https://www.youtube.com/watch?v=ZbZSe6N_BXs
    
            #sry to interupt but wats the city skilines music u listen to called
            # ummmm 
            # It's Cities: Skylines 1 Mars Radio
            # Ill send a link
            # :>
            # https://www.youtube.com/playlist?list=PLWkwE9lE45_m8wi256bF7FrEAininN30x yipeee
            # do you have apple music nah its fine 
            

    
    post_graph_ui()

# Physics Simulator
def physics_simulator():
    # INITIALIZE
    clear()
    logo("cALLculator > Math > Physics Simulator > Loading...")
    print("-"*100)
    for i in range(20):
        print()
    print("="*100)
    cube = object(10, coordinate(0, 20), 10)

    
    while True:
        # Header
        clear()
        logo("cALLculator > Math > Physics Simulator")
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
    custom_logo("| Made Possibley", "| Replit, Python")
    custom_logo("| Visual Graphing From", "| Matplotlib")
    custom_logo("| Math Tools From", "| Math & Random Library")
    custom_logo("| Search Made Possible By", "| Difflib")
    custom_logo("| Also", "| Numpy, Threading, Time, OS")
    custom_logo("| Biggest Thanks To", "| You, for checking this out!")

    home()

def basic_calc():
    logo("cALLculator > 4-Function Calculator")
    def print_calc(selected):
        print("_"*4)



#  _______________________
# |▒▒▒▒▒▒▒|       |       |       |
# |▒▒▒1▒▒▒|   2   |   3   |   /   |
# |▒▒▒▒▒▒▒|       |       |       |
# |       |       |       |       |
# |   4   |   5   |   6   |   x   |
# |       |       |       |       |
# |▒▒▒▒▒▒▒|       |       |       |
# |▒▒▒7▒▒▒|   8   |   9   |   -   |
# |▒▒▒▒▒▒▒|       |       |       |
# 
def home():
    clear()
    logo("cALLculator > Home")
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
            bal(constant, ax, h)
        case "about":
            print("About")
        case "credits": 
            credit()
            
    
home()




def about():
    clear()




