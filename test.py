def infos_perso():
    nom = input("Entrez votre nom : ")
    pnom = input("Entrez votre prénom : ")
    age = int(input("Entrez votre âge : "))
    taille = float(input("Entrez votre taille en cm : "))
    fruit = input("Entrez ton fruit préféré : ")
    return nom, age, taille, fruit
    
def show_infos_perso(nom, age, taille, fruit):
    print('\n-------------------------  REACP INFOS -----------------------')
    print("Nom:", nom)
    print("Age:", age, "ans")
    print("Taille:", taille, "cm")
    print("Fruit préféré:", fruit)

def salutation(nom):
    nom_majuscules = nom.upper()
    return ("Salut " + nom_majuscules + ", on est ravi de te revoir.\n Tes fruits préferés sont : " + fruit)

nom, age, taille, fruit = infos_perso()

show_infos_perso(nom, age, taille, fruit)
print(salutation(nom))
