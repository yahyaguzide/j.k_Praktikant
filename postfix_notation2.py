def IstRechnung(u):
    for i in u: 
        if i not in "+-/*123456789 ": 
            return False
    return True

def Rechner(nu1,nu2,op):
    ergebniss = 0
    if op == '+':
        ergebniss = nu1 + nu2
    elif op == "-":
        ergebniss = nu1 - nu2
    elif op == "/":
        ergebniss = nu1 / nu2
    elif op == "*":
        ergebniss = nu1 * nu2
    return ergebniss

while (True):
    c = input("Gebe eine Rechnung an ")
    a =  c.split(" ")
    b = []

    if a[0] == "quit" or a[0]  =="q":
        break
    elif not IstRechnung(c):
        print("Bitte verwende nur Zahlen")
    else:
        num1 = 0
        num2 = 0
        try:
            num1 = int(a[0])
            num2 = int(a[1])
        except:
            print("Bitte in der richtigen Form eingeben")
    
        print("Das Ergebniss ist " + str(Rechner(num1,num2,a[2])))      
        
