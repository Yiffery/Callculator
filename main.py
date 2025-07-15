# Python thingy majigy

import os
import time
def loadingScreen(task, number, total):
    # Callculator
    os.system('clear')
    print(r"   ____      _ _            _       _             ")
    print(r"  / ___|__ _| | | ___ _   _| | __ _| |_ ___  _ __ ")
    print(r" | |   / _` | | |/ __| | | | |/ _` | __/ _ \| '__|")
    print(r" | |__| (_| | | | (__| |_| | | (_| | || (_) | |   ")
    print(r"  \____\__,_|_|_|\___|\__,_|_|\__,_|\__\___/|_|   ")
    print()
    print(" | Callculator 0.1 Alpha")
    print(" | \x1B[3mDeveloped by Yifei & Yiran\x1B[0m")
    print()
    print(" > Loading: ", task)
    print("[", "="*round((number/total)*10), " "*(10-round((number/total*10))), "] ", str(round(number/total*100)), "%" )



for i in range (0,10):
    loadingScreen("test", i+1, 10)
    time.sleep(1)