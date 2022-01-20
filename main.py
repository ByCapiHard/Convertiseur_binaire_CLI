run= True
while run == True:
    try:
        choix = int(input("\nBienvenue dans notre convertiseur Binnaire/Hexadécimal \n 1= Binaire \n 2= Hexadécimal \n 3= Quitter\nSaisiez votre option: "))
        if choix == 1:
            nombre=int(input("Vous avez choisi de convertir en binnaire  \nSaisiez votre valeur :"))
            if nombre >= 0:
                convertion_final=bin(nombre)
                print("La convertion du chiffre est de : " + convertion_final[2:] )
            elif nombre <0:
                convertion_final=bin(nombre)
                print("La convertion du chiffre est de : -" + convertion_final[3:])
        elif choix == 2:
            nombre=int(input("Vous avez choisi de convertir en Hexadécimal \nSaisiez votre valeur : "))
            if nombre > 0:
                convertion_final=hex(nombre)
                print("La convertion du chiffre est de : " + convertion_final[2:] )
            elif nombre < 0:
                convertion_final=hex(nombre)
                print("La convertion du chiffre est de : -" + convertion_final[3:] )
        elif choix == 3:
            run = False
        else:
            print("Ta demande ne peux pas être traiter ! Assurer vous de bien selectioné la bonne valeur ")
    except ValueError:
        print("Pardon ! On a pas compris votre demande")
