#5.5 review this is challenge 36 of the UTCP CODING BOOKLET
import time
import os
while True:
    uname = input("Enter Username\n>>> ")
    if len(uname) >= 8:
        print("Welcome "+uname)
        time.sleep(2)
        os.system("clear")
        break
    else:
        print("Username Too Short")