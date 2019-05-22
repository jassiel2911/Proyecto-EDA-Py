import archivos as arch

def sumar_complejos():
    print("Ingrese primer complejo")
    n = complex(input())
    print("Ingrese segundo complejo")
    m = complex(input())
    resultado = n + m
    arch.archivo(resultado)
    return resultado

def restar_complejos():
    print("Ingrese primer complejo")
    n = complex(input())
    print("Ingrese segundo complejo")
    m = complex(input())
    resultado = n - m
    arch.archivo(resultado)
    return resultado

def producto_complejos():
    print("Ingrese primer complejo")
    n = complex(input())
    print("Ingrese segundo complejo")
    m = complex(input())
    resultado = n * m
    arch.archivo(resultado)
    return resultado

def dividir_complejos():
    try:
        print("Ingrese primer complejo")
        n = complex(input())
        print("Ingrese segundo complejo")
        m = complex(input())
        resultado = n / m
        arch.archivo(resultado)
        return resultado
    except ZeroDivisionError:
        print("Error Matematico\n")
        arch.archivo("Error Matematico")

def potecia_complejos():
    print("Ingrese primer complejo")
    n = complex(input())
    print("Ingrese potencia")
    k = complex(input())
    resultado = pow(n,k)
    arch.archivo(resultado)
    return resultado

def menu_complejos():
    while True:
            print("1. Suma de complejos")
            print("2. Resta de complejos")
            print("3. Producto de complejos")
            print("4. Division de complejos")
            print("5. Potencia de complejos")
            print("6. Regresar")
            opcion_complejos = input("Que desea hacer: ")
            if opcion_complejos == "Regresar" or opcion_complejos == 6:
                break
            elif opcion_complejos == "Suma" or opcion_complejos == 1:
                print("\n")
                print(sumar_complejos())
                print("\n")
            elif opcion_complejos == "Resta" or opcion_complejos == 2:
                print("\n")
                print(restar_complejos())
                print("\n")
            elif opcion_complejos == "Producto" or opcion_complejos == 3:
                print("\n")
                print(producto_complejos())
                print("\n")
            elif opcion_complejos == "Division" or opcion_complejos == 4:
                print("\n")
                print(dividir_complejos())
                print("\n")
            elif opcion_complejos == "Potencia" or opcion_complejos == 5:
                print("\n")
                print(potecia_complejos())
                print("\n")
            else: 
                print("Comando no reconocido\n")
