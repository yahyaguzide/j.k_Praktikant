import os
class Banane:
    count = 0
    def __init__(self, Obst_Gemüse, Preis):
        Banane.Obst_Gemüse = Obst_Gemüse
        Banane.Preis = Preis
    def __str__(self):
        return "1"

class Apfel:
    count = 0
    def __init__(self, Obst_Gemüse, Preis):
        self.Obst_Gemüse = Obst_Gemüse
        self.Preis = Preis
        Apfel.count = Apfel.count + 1
    def __str__(self):
        return "Ich bin ein Apfel /n es gibt " + str(Apfel.count) + "Äpfel"   

class Brokkoli:
    def __init__(Brokkoli, Obst_Gemüse, Preis):
        Brokkoli.Obst_Gemüse = Obst_Gemüse
        Brokkoli.Preis = Preis
    def __str__(self):
        return "Ich bin ein Brokkoli"    
class Einkaufsliste:
    a = "Banane wurde zur Einkaufsliste hinzugefügt"
    x = "Apfel wurde zur Einkaufsliste hinzugefügt"
    c = "Brokkoli wurde zur Einkaufsliste hinzugefügt"
liste = []
p1 = Einkaufsliste()
while(True):
    os.system("clear")
    s = input ("Du bist im Markt,aktuel haben wir die Produkte\nBanane\nBrokkoli\nApfel\nEingabe: ")
    if s == "Apfel":
        liste.append(Apfel("Obst", 5))
        print(p1.a)
    elif s == "Banane":
        liste.append(Banane("Obst", 4))
        print(p1.x)
    elif s == "Brokkoli":
        liste.append(Brokkoli("Gemüse", 9))
        print(p1.c)
    elif s == "Einkaufsliste":
        for produkt in liste:
            print(produkt)
        input("zum weiter einkaufen Enter klicken")
    else:
        print("Es gibt nur Äpfel,Bananen und Brokkoli auf dem Markt")
    
