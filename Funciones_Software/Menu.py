import random
import os
from Funciones import *

fin = True

while fin == True:
    os.system('clear')
    print('=' * 45)
    opcion = input('Bienvenido al Programa \n Ingrese 1 --> Para rectas paralelas y perpendiculares a una dada \n Ingrese 2 --> Para análisis de una Función Lineal \n Ingrese 3 --> Para análisis de una función cuadrática\n Ingrese 4 --> Sucesiones aritméticas\n Ingrese 5 --> Sucesiones geométricas \n Ingrese 6 --> salir del sistema.\n¿Qué opción deseas realizar?: ')
   
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
            
        elif opcion == 4:
            os.system('clear')
            print('Sucesiones aritmeticas: Una sucesión es aritmética cuando cada término se obtiene sumando un número al término que le precede.\nLa fórmula de una sucesión aritmética se expresa de la siguiente manera: an = a₁ + (n - 1) * d')
            while True:
                try:
                    termino_general = input('Ingrese el término general: ')
                    diferencia = input('Ingrese la diferencia: ')
                    terminos_conocer = int(input('Ingrese la cantidad de terminos que quiere conocer de la sucesión: '))
                    a = Fraction(termino_general)
                    b = Fraction(diferencia)
                    sucesion_aritmetica(a, b, terminos_conocer)
                except ValueError:
                    print('Ingreso invalido, intente nuevamente.')
                    continue
                else:
                    break
            input("Presiona Enter para continuar...")

        elif opcion == 5: 
            os.system('clear')
            print('Sucesion geométrica: Una sucesión geométrica o es una sucesión en la que cada término "an" se obtiene multiplicando al término anterior "an-1" por un número llamado razón.\nLa fórmula de una sucesión geométrica se expresa de la siguiente manera: an = a₁ * (n - 1) ** r')
            while True:
                try:
                    termino_general = float(input('Ingrese el término general: '))
                    razon = float(input('Ingrese la razón (La razón de una sucesión geométrica se denota por r y debe ser constante en toda la sucesión): '))
                    terminos_conocer = int(input('Ingrese la cantidad de terminos que quiere conocer de la sucesión: '))
                    sucesion_geometrica(termino_general, razon, terminos_conocer)
                except ValueError:
                    print('Ingreso invalido, intente nuevamente.')
                    continue
                else:
                    break
            input("Presiona Enter para continuar...")
        elif opcion == 6:
            fin = False 
            print('Gracias por usar nuestro sistema')

    else:
        os.system('clear')
        print('=' * 45)
        print('Opción No programada, intente nuevamente')
        print('=' * 45)