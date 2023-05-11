import random
import os
from Funciones import *


while True:
    print('=' * 45)
    opcion = input('Bienvenido al Programa \n Ingrese 1 - Para rectas paralelas y perpendiculares a una dada \n Ingrese 2 - Para análisis de una Función Lineal \n Ingrese 3 - Para análisis de una función cuadrática \n ¿Qué opción deseas realizar?: ')
   
    if esNumero(opcion) == True:
        
        opcion = int(opcion)
        
        if opcion == 1 or opcion == 2:
            os.system('clear')
            print('=' * 45)
            
            print('Estás en la opción ' + str(opcion) + '. Elige dos números. Uno será el coeficiente principal y el otro será el término independiente.')
        
            print('=' * 45)
            
            while True:
                try:
                    a = (input('Ingrese el coeficiente principal:'))
                    cPrincipal = Fraction(a)   
                    if cPrincipal == 0:
                        continue
                except ValueError:
                    print('Ingreso invalido, ingrese un numero')
                    continue
                else:
                    break
        
            while True:
                try:
                    b = (input('Ingrese el termino independiente:'))
                    tIndependiente = Fraction(b)
                except ValueError:
                    print('Ingreso invalido, ingrese un numero')
                    continue
                else:
                    break
                        
            if opcion == 1:
                os.system('clear')
                print('=' * 45)
                print("La condición de paralelismo entre dos rectas es que el coeficiente principal se mantenga y el término independiente cambie. \nEjemplos de ecuaciones con rectas paralelas a la dada son:")
                rectaParalela(cPrincipal,tIndependiente)
                print('=' * 45)
                print("La condición de perpendicularidad entre dos rectas es que la pendiente sea inversa y opuesta, mientras que el término independiente puede cambiar o no hacerlo. \nEjemplos de ecuaciones con rectas perpendiculares a la dada son:")
                rectaPerpendicular(cPrincipal, tIndependiente)
                print('=' * 45 )
                print('Otros ejemplos de perpendicularidad son: ')
                rectaPerpendicular2(cPrincipal, tIndependiente) 
                print('=' * 45 )
                           
            elif opcion == 2:
                os.system('clear')
                while True:
                    try:
                        recta(cPrincipal,tIndependiente)
                    except ZeroDivisionError:
                        print('No es posible dividir por cero')
                        break
                    else:
                        break
                    
        elif opcion == 3:
            os.system('clear')
            print('=' * 45)          
            print('Estás en la opción 3. Elige tres números. Uno será el coeficiente principal, el segundo será el coeficiente lineal y el tercero será el término independiente.')
            print('=' * 45)
            
            while True:
                try:
                    a = (input('Ingrese el coeficiente principal:'))
                    cPrincipal = Fraction(a)
                    if cPrincipal == 0:
                        print('El coeficiente principal tiene que ser distinto a cero, intenta nuevamente.')
                        continue     
                except ValueError:
                    print('Ingreso invalido, ingrese un numero')
                    continue
                else:
                    break
                
            while True:
                try:
                    b = (input('Ingrese el coeficiente lineal:'))
                    cLineal = Fraction(b) 
                except ValueError:
                    print('Ingreso invalido, ingrese un numero')
                    continue
                else:
                    break
                
            while True:
                try:
                    c = (input('Ingrese el término independiente:'))
                    tIndependiente = Fraction(c) 
                except ValueError:
                    print('Ingreso invalido, ingrese un numero')
                    continue
                else:
                    break
                            
            parabola(cPrincipal, cLineal, tIndependiente)
     
                 
    else:
        os.system('clear')
        print('=' * 45)
        print('Opción No programada, intente nuevamente')
        print('=' * 45)