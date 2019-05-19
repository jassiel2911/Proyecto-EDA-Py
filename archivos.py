def archivo(resultado):
    try:
        f = open("resultados.txt", "a")
        f.write(str(resultado)+"\n")
    finally:
        f.close()