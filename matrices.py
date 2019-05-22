import numpy as np
import sys
import archivos as arch

def sumar_matrices():

    r1=int(input("Numero de filas de M1: "))
    c1=int(input("Numero de columnas de M1: "))
    r2=int(input("\nNumero de filas de M2: "))
    c2=int(input("Numero de columnas de M2: "))

    mat1=np.zeros((r1,c1))
    mat2=np.zeros((r2,c2))
    mat3=np.zeros((r1,c2))

    print("Introduce la primera matriz: \n")

    for r in range(0,r1):
        for c in range(0,c1):
            mat1[r,c]=input("Captura M1: ["+str(r+1)+str(c+1)+"]")

    print("Introduce la segunda matriz: \n")
    
    for r in range(0,r2):
        for c in range(0,c2):
            mat2[r,c]=input("Captura M2: ["+str(r+1)+str(c+1)+"]")

    #Operacion suma

    for r in range(0,r1):
        for c in range(0,c2):
            mat3[r,c]+=mat1[r,c]+mat2[r,c]

    print(mat3)
    arch.archivo(mat3)

def restar_matrices():

    r1=int(input("Numero de filas de M1: "))
    c1=int(input("Numero de columnas de M1: "))
    r2=int(input("\nNumero de filas de M2: "))
    c2=int(input("Numero de columnas de M2: "))

    mat1=np.zeros((r1,c1))
    mat2=np.zeros((r2,c2))
    mat3=np.zeros((r1,c2))

    print("Introduce la primera matriz: \n")

    for r in range(0,r1):
        for c in range(0,c1):
            mat1[r,c]=input("Captura M1: ["+str(r+1)+str(c+1)+"]")

    print("Introduce la segunda matriz: \n")
    
    for r in range(0,r2):
        for c in range(0,c2):
            mat2[r,c]=input("Captura M2: ["+str(r+1)+str(c+1)+"]")

    #Operacion resta

    for r in range(0,r1):
        for c in range(0,c2):
            mat3[r,c]+=mat1[r,c]-mat2[r,c]

    print(mat3)
    arch.archivo(mat3)


def multiplicar_matrices():

    r1=int(input("Numero de filas de M1: "))
    c1=int(input("Numero de columnas de M1: "))
    r2=int(input("\nNumero de filas de M2: "))
    c2=int(input("Numero de columnas de M2: "))

    if (c1 != r2):
        print("No se puede hacer el producto matricial\n")
        arch.archivo("No se puede hacer el producto matricial")
    else:
        mat1=np.zeros((r1,c1))
        mat2=np.zeros((r2,c2))
        mat3=np.zeros((r1,c2))

        print("Introduce la primera matriz: \n")

        for r in range(0,r1):
            for c in range(0,c1):
                mat1[r,c]=input("Captura M1["+str(r+1)+str(c+1)+"]")

        print("Introduce la segunda matriz: \n")

        for r in range(0,r2):
            for c in range(0,c2):
                mat2[r,c]=input("Captura M2["+str(r+1)+str(c+1)+"]")

        #Operacion producto

        for r in range(0,r1):
            for c in range(0,c2):
                for k in range (0,r2):
                    mat3[r,c]+=mat1[r,k]*mat2[k,c]

        print(mat3)
        arch.archivo(mat3)

def multiplicacion_escalar():

    r1=int(input("Numero de filas de M1: "))
    c1=int(input("Numero de columnas de M1: "))
    escalar=int(input("Escalar a multiplicar: "))

    mat1=np.zeros((r1,c1))
    matr=np.zeros((r1,c1))

    print("Introduce la matriz: \n")

    for r in range(0,r1):
        for c in range(0,c1):
            mat1[r,c]=input("Captura de matriz: ["+str(r+1)+str(c+1)+"]")

    #Operacion

    for r in range(0,r1):
        for c in range(0,c1):
            matr[r,c]=mat1[r,c]*escalar
        
    print(matr)
    arch.archivo(matr)

def menu_matrices():
    while True:
            print("1. Suma de matrices")
            print("2. Resta de matrices")
            print("3. Producto de matrices")
            print("4. Producto por escalar de matrices")
            print("5. Regresar")
            opcion_matrices = input("Que desea hacer: ")
            print("\n")
            if opcion_matrices == "Regresar" or opcion_matrices == 5:
                break
            elif opcion_matrices == "Suma" or opcion_matrices == 1:
                print("\n")
                sumar_matrices()
                print("\n")
            elif opcion_matrices == "Resta" or opcion_matrices == 2:
                print("\n")
                restar_matrices()
                print("\n")
            elif opcion_matrices == "Producto" or opcion_matrices == 3:
                print("\n")
                multiplicar_matrices()
                print("\n")
            elif opcion_matrices == "Producto por escalar" or opcion_matrices == 4:
                print("\n")
                multiplicacion_escalar()
                print("\n")
            else:
                print("\nComando no reconocido\n")
