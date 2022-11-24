#find circumferene/area of circle
import time
import tkinter as tk

wants = input("What  would you like to do? \n Enter [1] for the area or circumferce of a circle finder. \n Press [2] for the GST Finder. \n Press [3] for the 3D object finder. \n Press [4] for the Area of a triangle finder. \n Press [5] for the fibonacci series. \n  ")

if wants == "1":
    pinumber = input("What would you like to be your pi value? Enter (1) for 22 over 7. Enter (2) for 3.14. \n")

    if pinumber == '1':
        pi = 22/7

    elif pinumber == '2':
        pi = 3.14

    type = input("Circumfence or Area? Enter (1) for circumferene. Enter (2) for Area\n")

    if type == '1':
        diameter = int(input("Diameter of circle? \n"))
        print (diameter * pi)
        time.sleep(3)

    elif type == '2':
        radius = int(input ("Radius of Circle? \n"))
        print (radius**2 * pi)
        time.sleep(3)

    else:
        print(" Try again! ")
        time.sleep(5)


if wants == "2":
    price = int(input("The price? \n"))
    typeofgst = input("107% or 7%? \n")
    GST = 0.07
    
    if typeofgst == '107%':
        print(price * GST + price)
        time.sleep(3)
    
    if typeofgst == '7%':
        print(price * GST)
        time.sleep(3)
    

if wants == "3":
    length = int(input("Length of said figure? \n"))
    width = int(input("Width of said figure? \n "))
    height = int(input("Height of said figure? \n "))
    print (length*width*height)
    time.sleep(3)

if wants == "4":
    base = int(input("Base of the triangle?"))
    height = int(input("Height of the triangle?"))
    print (base*height/2)
    time.sleep(3)

if wants == "5":
    maxnumber = int(input("Max Number?"))
    a, b = 0, 1
    while a < maxnumber:
        print (a)
        a, b = b, a+b
        time.sleep(3)

else:
    a = 1000
    b = 1001
    def spam():
        print("No lol")
        print(" No lol")
        print("  No lol")
        print("   No lol")
        print("    No lol")
        print("     No lol")
        print("      No lol")
        print("        No lol")
        print("         No lol")
        print("          No lol")
        print("           No lol")

        spamStr = "Swiper, no swiping!"

        window = tk.Tk()
        text = tk.Label(text = spamStr)
        text.pack()

        window1 = tk.Tk()
        text1 = tk.Label(text = "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        text.pack()
        window1 = tk.Tk()
        window1 = tk.Tk()
        window1 = tk.Tk()
        window1 = tk.Tk()
        window1 = tk.Tk()
        window1 = tk.Tk()
        window1 = tk.Tk()
        window1 = tk.Tk()
        window1 = tk.Tk()
        window1 = tk.Tk()
        window1 = tk.Tk()
        window1 = tk.Tk()
        window1 = tk.Tk()
        window1 = tk.Tk()
        window1 = tk.Tk()
        window1 = tk.Tk()
        window1 = tk.Tk()
        window1 = tk.Tk()
        window1 = tk.Tk()
        window1 = tk.Tk()
        window1 = tk.Tk()
        window1 = tk.Tk()
        window1 = tk.Tk()
        window1 = tk.Tk()
        window1 = tk.Tk()
        window1 = tk.Tk()
        window1 = tk.Tk()
        window1 = tk.Tk()
        window1 = tk.Tk()
        window1 = tk.Tk()
        window1 = tk.Tk()
        window1 = tk.Tk()

        window.mainloop()



    while a < b:
        b = b+1
        spam()

        
