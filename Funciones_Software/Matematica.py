#Desarrollar un software que cumpla los siguientes requerimientos:

#Debe contar con un menú que permita seleccionar entre las siguientes opciones:

#Rectas paralela y perpendicular a una dada.
#Análisis de una función lineal.
#Análisis de una función cuadrática.

#Rectas paralela y perpendicular a una dada. En esta opción el usuario deberá ingresar por teclado el coeficiente principal 
#y el término independiente. Se deberá mostrar por pantalla al menos 3 (tres) rectas paralelas y 3 (tres) perpendiculares. 
#No se permite que el sistema arroje como resultado de alguna de las consignas la misma recta ingresada por el usuario. 
#Además como información en pantalla deberá enunciarse la condición de paralelismo y también la de perpendicularidad.

#Análisis de una recta. En esta opción el usuario deberá ingresar por teclado el coeficiente principal y el término independiente. 
#Se deberá mostrar por pantalla la siguiente información: corte con el eje x, corte con el eje y, comportamiento de la recta (creciente o decreciente).

#Análisis de una parábola. En esta opción el usuario deberá ingresar por teclado el coeficiente principal, el coeficiente lineal y 
# el término independiente. Se deberá mostrar por pantalla la siguiente  información: corte con el eje x, corte con el eje y, 
# intervalo de crecimiento e intervalo de decrecimiento, coordenadas del vértice, concavidad de la parábola 
# (cóncava hacia arriba o cóncava hacia abajo). Además deberá informarse en el caso que la parábola no posea soluciones 
# reales como así también cuando la solución tenga doble multiplicidad.
import os
import random 
from Funciones import *

bandera = 0 
contador = 0


while bandera == 0:
    opcion = int(input('Bienvenido al Programa \n Ingrese 1 - Para rectas paralelas y perpendiculares a una dada \n Ingrese 2 - Para analisis de una Funcion Lineal \n Ingrese 3 - Para Analisis de una funcion cuadratica \n Que opcion deseas realizar? :'))
    if opcion == 1:
        bandera = 1
        print('Estas en la opcion uno, elige dos numeros uno sera el coeficiente principal y otro el termino independiente, luego generare 3 rectas paralelas y 3 perpendiculares.')
        
        cPrincipal = int(input('Ingresa el coeficiente principal: '))
        if cPrincipal == 0:
            print('El coeficiente principal tiene que ser mayor a cero, ingresa un numero mayor a cero')
            cPrincipal = int(input('Ingresa el coeficiente principal: '))
        
        tIndependiente = int(input('Ingresa el termino independiente: '))
        
        print("La condicion de paralelismo es que el coheficiente principal se mantenga y el termino independiente sea el que cambie. \nEjemplos de ecuaciones con rectas paralelas a la dada son:")
        rectaParalela(cPrincipal,tIndependiente)
        print('--------------------------------------------------------')
        print("La condicion de perpendicularidad es que la pendiente debe ser inversa y opuesta, el termino independiente puede cambiar o no hacerlo. \nEjemplos de ecuacion con rectas perpendiculares a la dada son:")
        rectaPerpendicular(cPrincipal, tIndependiente)
        print('------------------------------------------')
        
            
                             
    elif opcion == 2:
        bandera = 1
        print('Estas en la opcion 1')
    elif opcion == 3:
        bandera = 1
        print('Estas en la opcion 1')
    else:
        bandera = 0
        