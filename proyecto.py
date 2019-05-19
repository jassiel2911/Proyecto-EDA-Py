import complejos as cx
import matrices as mat
import polinomios as pol

print("\n\t\t\t\t===========")
print("\t\t\t\tCALCULADORA")
print("\t\t\t\t===========\n")

while True:
    print("1. Complejos")
    print("2. Polinomios")
    print("3. Matrices")
    print("4. Salir")
    opcion = input("Que desea hacer: ")
    print("\n")
    if opcion == "Salir" or opcion == 4:
        break
    elif opcion == "Complejos" or opcion == 1:
        cx.menu_complejos()
    elif opcion == "Polinomios" or opcion == 2:
        pol.menu_polinomios()
    elif opcion == "Matrices" or opcion == 3:
        mat.menu_matrices()
    else:
        print("Comando no reconocido\n")