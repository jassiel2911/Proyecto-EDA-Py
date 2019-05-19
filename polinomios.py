import sympy
import archivos as arch

sympy.init_printing()
x = sympy.symbols('x')

def suma(P1,P2):
    return P1+P2

def resta(P1,P2):
    return P1-P2

def multi(P1,P2):
    return P1*P2

def pot(P1,P):
    P3=P1
    for i in range(1,P,1):
        P3=P3*P1
    return P3

def menu_polinomios():
    while True:
        print("1. Suma de polinomios")
        print("2. Resta de polinomios")
        print("3. Multiplicacion de polinomios")
        print("4. Potencia de polinomios")
        print("5. Regresar")
        opcion_polinomios = input("Que desea hacer: ")
        print("\n")
        if opcion_polinomios == "Regresar" or opcion_polinomios == 5:
            break
        elif opcion_polinomios == "Suma" or opcion_polinomios == 1:
            P1 = input("Primer polinomio: ")
            P2 = input("Segundo polinomio: ")
            print("\n")
            Poly1 = sympy.Poly(P1)
            Poly2 = sympy.Poly(P2)
            print("Resultado: ", suma(Poly1,Poly2))
            arch.archivo(suma(Poly1,Poly2))
            print("\n")
        
        elif opcion_polinomios == "Resta" or opcion_polinomios == 2:
            P1 = input("Primer polinomio: ")
            P2 = input("Segundo polinomio: ")
            print("\n")
            Poly1 = sympy.Poly(P1)
            Poly2 = sympy.Poly(P2)
            print("Resultado: ", resta(Poly1,Poly2)) 
            arch.archivo(resta(Poly1,Poly2))
            print("\n")       

        elif opcion_polinomios == "Multiplicacion" or opcion_polinomios == 3:
            P1 = input("Primer polinomio: ")
            P2 = input("Segundo polinomio: ")
            print("\n")
            Poly1 = sympy.Poly(P1)
            Poly2 = sympy.Poly(P2)
            print("Resultado: ", multi(Poly1,Poly2))
            arch.archivo(multi(Poly1,Poly2))
            print("\n")
        
        elif opcion_polinomios == "Potencia" or opcion_polinomios == 4:
            P1 = input("Primer polinomio: ")
            P = int(input("Potencia: "))
            print("\n")
            Poly1 = sympy.Poly(P1)
            resultado = pot(Poly1,P)
            print("Resultado: ", resultado)
            arch.archivo(resultado)
            print("\n")
                
        else:
            print("Comando no reconocido\n")