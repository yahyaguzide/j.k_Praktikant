from os import system as console
import time

def HasDigit(w):
    for i in w:
    if i == "+":
        return False
        if i.isdigit():
            return True
    else return False

def HasChar(w,c = "e"):
    if c in w:
        return True
    return False

def TextRoll(srg = "test"):
    Tr = srg + "          "
    while(True):
        console("clear")
        print(Tr)
        Buffer = Tr[len(Tr)-1]
        Tr = Buffer + Tr[:len(Tr)-1]
        time.sleep(0.5)

s = "" 
while(s == ""):   
    s = input("Bitte eine eingabe machen: ")

TextRoll(s)

if HasDigit(s) :
    print("Bitte keine zahlen verwenden")
else: 
    print("Hello " + s + "!")
if HasChar(s):
    print("Es gibt ein e")
