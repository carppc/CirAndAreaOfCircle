import time as t
import tkinter as tk
def areaGUI():
    def ARconf():  
        radius = entRad.get()
        radius = int(radius)
        pi = piEnt.get()
        pi = float(pi)
    
        area = radius **2 * pi
        result = tk.Label(
            text = area,
            height = 1,
        )
        result.pack()
    #window = tk.Tk()
    #window.title("Area of Circle")
    #window setup

    SIZ = int(5)
    MainF = tk.Frame(borderwidth=1)

    labRad = tk.Label(
        text = "Radius",
        master = MainF,
        height = 2,
        width = 5,
    )
    labRad.grid(row = 0, column = 0)
    entRad = tk.Entry(width = 10,master = MainF)
    entRad.grid(row = 1, column = 0, sticky = 'e')

    labPi = tk.Label(
        text = "Pi",
        master = MainF,
        height = 2,
        width = 5,
    )
    labPi.grid(row = 0, column = 1)
    piEnt = tk.Entry(width = 10,master = MainF)
    piEnt.grid(row = 1, column = 1)
    
    ARcon = tk.Button(
        text = "confirm",
        height = 2,
        width = 5,
        command = ARconf,
        master = MainF,
    )
    ARcon.grid(row = 1, column = 2)
    MainF.pack()
    #window.mainloop()

def CirGUI():
    def CIConf():
        diameter = entDia.get()
        diameter = int(diameter)
        pi = entPi.get()
        pi = float(pi)
        
        cir = diameter * pi
        result = tk.Label(
            text = cir,
            height = 2,
        )
        result.pack()
    #window = tk.Tk()
    #window.title("Circumfernce of Circle")
    MainF = tk.Frame()
    
    labDia = tk.Label(
        text = "Diameter",
        height = 3,
        width = 10,
        master = MainF,
    )
    labDia.grid(row = 0, column = 0)
    entDia = tk.Entry(width = 10,master = MainF)
    entDia.grid(row = 1, column = 0)
    
    labPi = tk.Label(
        text = "Pi",
        height = 3,
        width = 10,
        master = MainF,
    )
    labPi.grid(row = 0, column = 1)
    entPi = tk.Entry(width = 10,master = MainF)
    entPi.grid(row = 1, column = 1)
    
    butCir = tk.Button(
        text = "confirm",
        height = 5,
        width = 5,
        master = MainF,
        command = CIConf,
    )
    butCir.grid(row =1, column = 2)
    
    MainF.pack()
    #window.mainloop()

Window = tk.Tk()
Window.title("Circumfernce and Area of Circle Finder")
FRA = tk.Frame()

AREbut = tk.Button(
    text = "Area",
    height = 5,
    width = 10,
    master = FRA,
    command = areaGUI,
)
AREbut.grid(row = 0, column = 1)

CIRbut = tk.Button(
    text = "Circumfernce",
    height = 5,
    width = 10,
    master = FRA,
    command = CirGUI,
)
CIRbut.grid(row = 0, column = 3)

FRA.pack()
Window.mainloop()