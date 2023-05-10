import random
import os
from Funciones import *
from FuncionesFracciones import *

while True:
    
    opcion = input('Bienvenido al Programa \n Ingrese 1 - Para rectas paralelas y perpendiculares a una dada \n Ingrese 2 - Para análisis de una Función Lineal \n Ingrese 3 - Para análisis de una función cuadrática \n ¿Qué opción deseas realizar?: ')
    
    if esNumero(opcion) == True:
        
        opcion = int(opcion)
        
        opcion2 = input('¿Te gustaría trabajar con fracciones? Ingresa 1 para Sí o 2 para No.')
        
        if esNumero(opcion2) == True:
            opcion2 = int(opcion2)
            if opcion2 == 1:
                fraccionesF(opcion) 
            else:
                if opcion == 1 or opcion == 2:
            
                    print('-_' * 45)
            
                    print('Estás en la opción ' + str(opcion) + '. Elige dos números. Uno será el coeficiente principal y el otro será el término independiente.')
        
                    print('-_' * 45)
            
                    while True:
                        try:
                            cPrincipal = float(input('Ingrese el coeficiente principal:'))   
                            if cPrincipal == 0:
                                print('El coeficiente principal tiene que ser mayor a cero, intenta nuevamente.')
                                continue
                        except ValueError:
                            print('Ingreso invalido, ingrese un numero')
                            continue
                        else:
                            break
                
                    while True:
                        try:
                            tIndependiente = Fraction(input('Ingrese el termino independiente:'))
                        except ValueError:
                            print('Ingreso invalido, ingrese un numero')
                            continue
                        else:
                            break
                        
                if opcion == 1:
                    print('-_' * 45)
                    print("La condición de paralelismo entre dos rectas es que el coeficiente principal se mantenga y el término independiente cambie. \nEjemplos de ecuaciones con rectas paralelas a la dada son:")
                    rectaParalela(cPrincipal,tIndependiente)
                    print('-_' * 45)
                    print("La condición de perpendicularidad entre dos rectas es que la pendiente sea inversa y opuesta, mientras que el término independiente puede cambiar o no hacerlo. \nEjemplos de ecuaciones con rectas perpendiculares a la dada son:")
                    rectaPerpendicular(cPrincipal, tIndependiente)
                    print('-_' * 45 )
                
                elif opcion == 2:
                    while True:
                        try:
                            recta(cPrincipal,tIndependiente)
                        except ZeroDivisionError:
                            print('No es posible dividir por cero')
                            break
                        else:
                            break
                    
        elif opcion == 3:
            print('-_' * 45)          
            print('Estás en la opción 3')
            print('-_' * 45)
            
            while True:
                try:
                    cPrincipal = float(input('Ingrese el coeficiente principal:'))   
                    if cPrincipal == 0:
                        print('El coeficiente principal tiene que ser mayor a cero, intenta nuevamente.')
                        continue
                except ValueError:
                    print('Ingreso invalido, ingrese un numero')
                    continue
                else:
                    break
                
            while True:
                try:
                    cLineal = float(input('Ingrese el termino independiente:'))
                except ValueError:
                    print('Ingreso invalido, ingrese un numero')
                    continue
                else:
                    break
                
            while True:
                try:
                    tIndependiente = float(input('Ingrese el termino independiente:'))
                except ValueError:
                    print('Ingreso invalido, ingrese un numero')
                    continue
                else:
                    break
                            
            parabola(cPrincipal, cLineal, tIndependiente)
     
                 
    else:
        print('-_' * 45)
        print('Opción No programada, intente nuevamente')
        print('-_' * 45)