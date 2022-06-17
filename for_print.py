s = input("Bitte eine eingabe machen: ")

hasdigit = False
for i in s:
    if i.isdigit():
        hasdigit = True
        #print(i + "ist eine zahl")
        break

if(s == ""):
    print("Die eingabe darf nicht leer sein")
    
elif hasdigit :
    print("Bitte keine Zahlen verwenden")

else:
    print("Hello " + s  + "!")
