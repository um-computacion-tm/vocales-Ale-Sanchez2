from ast import While
import unittest

#agregar mayusculas y minusculas 

def contar_vocales(palabra):
    resultado ={}
    for letra in palabra:
        if letra in 'aeiouAEIOUáéíóúÁÉÍÓÚ':
            if letra not in resultado:
                resultado[letra] = 0
            resultado[letra] +=1
    return resultado





if __name__ == "__main__":

    while True:
        Palabra= contar_vocales(input("Ingrese una palabra: "))
        print(Palabra)
        seguir = input("Desea seguir? (s/n): ")
        if seguir != "s":
            break
        
    