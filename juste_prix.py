import random


print("trouver le prix de l'objet X")
prix=random.randint(1,10)
#print(f"prix = {prix}")

essais = 0

while essais < 5:
    print(f"nombre d'essais restant : {5 - essais}")
    proposition = int(input("propose un nombre entre 1 et 10\n"))
    essais = essais + 1
    if proposition < 1 or proposition > 10:
        print("bruh entre 1 et 10 :-|")
        exit()
    if proposition == prix:
        print("bonne réponse!")
        exit()
    elif proposition > prix:
        print("nope! >:) c'est moins")
    else:
        print("c'est plus")

if essais >= 5:
    print(f"perduuuuuuu c'était {prix} :)")
    exit()