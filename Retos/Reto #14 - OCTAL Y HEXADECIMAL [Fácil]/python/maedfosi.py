#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math

code = {1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9",10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}


def ask():
    conv = str(input("¿Qué conversión quieres obtener?: 1.Hexadecimal, 2.Octal \n Seleccion: "))
    decision(conv)

def decision(conv):
    if conv == "1":
        tipo = "hexadecimal"
        divisor = 16
        conversion(divisor, tipo)
        ask()
    elif conv == "2":
        tipo = "octal"
        divisor = 8
        conversion(divisor, tipo)
        ask()
    else:
        print("Haz una selección valida: 1. Hexadecimal, 2. Octal")
        ask()

#Usamos la misma función para las dos conversiones

def conversion(divisor, tipo):
    num_dec = int(input("ingresar un número decimal: "))
    prev_hexa = []
    prev_hexa.append(str(num_dec%divisor))
    ld = str(num_dec%divisor)
    while num_dec/divisor >= 1:
        num_dec = num_dec/divisor
        res = math.floor(num_dec%divisor)
        codi = code.get(res)
        prev_hexa.append(str(codi))
    print("El número", tipo, "es: ",str("".join(prev_hexa[::-1])))

ask()

