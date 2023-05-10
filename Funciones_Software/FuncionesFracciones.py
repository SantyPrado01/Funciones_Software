from fractions import Fraction
from Funciones import *
def fraccionesF(opcion):
    if opcion == 1 or opcion == 2:
            
        print('-_' * 45)
            
        print('Estás en la opción ' + str(opcion) + '. Elige dos números. Uno será el coeficiente principal y el otro será el término independiente.')
        
        print('-_' * 45)
            
        while True:
            try:
                cPrincipal = (input('Ingrese el coeficiente principal:'))
                cPrincipalF = Fraction(cPrincipal)   
                if cPrincipalF == 0:
                    print('El coeficiente principal tiene que ser mayor a cero, intenta nuevamente.')
                    continue
            except ValueError:
                print('Ingreso invalido, ingrese un numero')
                continue
            else:
                break
                
        while True:
            try:
                tIndependiente = (input('Ingrese el termino independiente:'))
                tIndependienteF = Fraction(tIndependiente)
            except ValueError:
                print('Ingreso invalido, ingrese un numero')
                continue
            else:
                break
                        
        if opcion == 1:
            print('-_' * 45)
            print("La condición de paralelismo entre dos rectas es que el coeficiente principal se mantenga y el término independiente cambie. \nEjemplos de ecuaciones con rectas paralelas a la dada son:")
            rectaParalela(cPrincipalF,tIndependienteF)
            print('-_' * 45)
            print("La condición de perpendicularidad entre dos rectas es que la pendiente sea inversa y opuesta, mientras que el término independiente puede cambiar o no hacerlo. \nEjemplos de ecuaciones con rectas perpendiculares a la dada son:")
            rectaPerpendicular(cPrincipalF, tIndependienteF)
            print('-_' * 45 )
                
        elif opcion == 2:
            while True:
                try:
                    recta(cPrincipalF,tIndependienteF)
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