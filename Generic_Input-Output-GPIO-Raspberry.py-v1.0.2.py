"""
GPIO Control Script in Python

This Python script use of the RPi.GPIO library to control GPIO pins on a Raspberry Pi. The script configures one GPIO pin as input, reading its state and printing the result. Additionally, it configures another GPIO pin as output, toggling its state between high and low.

Requirements:
- Raspberry Pi with RPi.GPIO library installed

Usage:
1. Connect a switch/button to the input GPIO pin.
2. Connect an LED to the output GPIO pin via a current-limiting resistor.
3. Run this script to read the input state and toggle the output state.

Note: Adjust GPIO pin numbers according to your hardware configuration.

Author: [Eduardo Valdez]
"""


import tkinter as tk
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

#Rele 1
GPIO.setup(17,GPIO.OUT)
GPIO.output(17,GPIO.HIGH)

#Rele 2
GPIO.setup(27,GPIO.OUT)
GPIO.output(27,GPIO.HIGH)

#Rele 3
GPIO.setup(5,GPIO.OUT)
GPIO.output(5,GPIO.HIGH)

#Rele 4
GPIO.setup(22,GPIO.OUT)
GPIO.output(22,GPIO.HIGH)

#SE1
GPIO.setup(26, GPIO.IN)

#SE2
GPIO.setup(16, GPIO.IN)

#SE3
GPIO.setup(13, GPIO.IN)

#SE4
GPIO.setup(6, GPIO.IN)


class LED(tk.Frame):
    def __init__(self, master, size=30, color_off="gray", color_on="red"):
        tk.Frame.__init__(self, master, width=size, height=size, borderwidth=1, relief="solid", bg=color_off)
        self.pack_propagate(False)

        # Inicializar el estado apagado
        self.state = False
        
        self.label = tk.Label(self, text="OFF", font=("Arial", 8), bg=color_off)
        self.label.place(relx=0.5, rely=0.5, anchor="center")

    def update_color(self, state):
        # Actualizar el color del LED según el estado
        color = "green" if state else "red"
        tetx = "ON" if state else "OFF"
        self.configure(bg=color)
        self.label.configure(bg=color, text=text)
        
def Rel_1():
    print("Out-1 presionado")
    if GPIO.input(17):
        GPIO.output(17,GPIO.LOW)
        print("Activando Out-1")
        Rele_1BOTON["text"] = "Out-1 ON"
        Rele_1BOTON["bg"] = "green"
        
    else:
        GPIO.output(17,GPIO.HIGH)
        print("Desactivando Out-1")
        Rele_1BOTON["text"] = "Out-1 OFF"
        Rele_1BOTON["bg"] = "red"  # Cambiar color a rojo
        
def Rel_2():
    print("Out-2 presionado")
    if GPIO.input(27):
        GPIO.output(27,GPIO.LOW)
        print("Activando Out-2")
        Rele_2BOTON["text"] = "Out-2 ON"
        Rele_2BOTON["bg"] = "green"
    else:
        GPIO.output(27,GPIO.HIGH)
        print("Desactivando Out-2")
        Rele_2BOTON["text"] = "Out-2 OFF"
        Rele_2BOTON["bg"] = "red"

def Rel_3():
    print("Out-3 presionado")
    if GPIO.input(5):
        GPIO.output(5,GPIO.LOW)
        print("Activando Out-3")
        Rele_3BOTON["text"] = "RELE 3 ON"
        Rele_3BOTON["bg"] = "green"
    else:
        GPIO.output(5,GPIO.HIGH)
        print("Desactivando Out-3")
        Rele_3BOTON["text"] = "Out-3 OFF"
        Rele_3BOTON["bg"] = "red"

def Rel_4():
    print("Out-4 presionado")
    if GPIO.input(22):
        GPIO.output(22,GPIO.LOW)
        print("Activando Out-4")
        Rele_4BOTON["text"] = "Out-4 ON"
        Rele_4BOTON["bg"] = "green"
    else:
        GPIO.output(22,GPIO.HIGH)
        print("Desactivando Out-4")
        Rele_4BOTON["text"] = "Out-4 OFF"
        Rele_4BOTON["bg"] = "red"
       
def SE_1():
    SE1 = GPIO.input(26)
    if (SE1 == True):
        print("in-1 activado")
        SE_1_LED.update_color(state)
        #time.sleep(0.3)
    else:
         print("in-1 desactivado")
         
def SE_2():
    SE2 = GPIO.input(26)
    if (SE2 == True):
        print("in-2 activado")
        #time.sleep(0.3)
    else:
         print("in-2 desactivado")
         
def SE_3():
    SE3 = GPIO.input(26)
    if (SE3 == True):
        print("in-3 activado")
        #time.sleep(0.3)
    else:
         print("in-3 desactivado")
         
def SE_4():
    SE4 = GPIO.input(26)
    if (SE4 == True):
        print("in-4 activado")
        #time.sleep(0.3)
    else:
         print("in-4 desactivado")
       
def salir():
    print("Bonton de salida presionado")
    GPIO.cleanup()
    ventana.destroy()
   
ventana = tk.Tk()
ventana.title("INPUT-OUTPUT")
ventana.geometry("400x400")

SlirButton = tk.Button(ventana,text = "SALIR",
                    command = salir,height = 2,width = 6)
SlirButton.place(x=165, y=295)


SE = tk.Label(ventana, text = "Outputs", fg="Blue",font=("Helvetica", 14))
SE.place(x=40, y=10)
#botones  reles
Rele_1BOTON = tk.Button(ventana,text = "Output 1",
                    command = Rel_1,height =  2,width = 8)
Rele_1BOTON.place(x=50, y=60)

Rele_2BOTON = tk.Button(ventana,text = "Output 2",
                    command = Rel_2,height = 2,width = 8)
Rele_2BOTON.place(x=50, y=115)

Rele_3BOTON = tk.Button(ventana,text = "Output 3",
                    command = Rel_3,height = 2,width = 8)
Rele_3BOTON.place(x=50, y=170)

Rele_4BOTON = tk.Button(ventana,text = "Output 4",
                    command = Rel_4,height = 2,width = 8)
Rele_4BOTON.place(x=50, y=235)


SE = tk.Label(ventana, text = "Inputs", fg="Blue",font=("Helvetica", 14))
SE.place(x=200, y=10)

SE1 = tk.Label(ventana, text = "Input 1")
SE1.place(x=215, y=40)

SE_1_LED = LED(ventana, size=30, color_off="red", color_on="green")
SE_1_LED.place(x=270, y=65)


SE2 = tk.Label(ventana, text = "Input 2")
SE2.place(x=215, y=100)

SE_2_LED = LED(ventana, size=30, color_off="red", color_on="green")
SE_2_LED.place(x=270, y=125)

SE3 = tk.Label(ventana, text = "Input 3")
SE3.place(x=215, y=160)

SE_3_LED = LED(ventana, size=30, color_off="red", color_on="green")
SE_3_LED.place(x=270, y=185)

SE4 = tk.Label(ventana, text = "Input 4")
SE4.place(x=215, y=220)

SE_4_LED = LED(ventana, size=30, color_off="red", color_on="green")
SE_4_LED.place(x=270, y=245)


ventana.mainloop()