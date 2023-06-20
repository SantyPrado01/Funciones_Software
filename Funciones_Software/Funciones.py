import random
from fractions import Fraction
from math import sqrt

def esNumero(a):
    if a.isnumeric():
        a = int(a)
        return(True)
    else:
        return(False)


def rectaParalela(a,b):
    cont = 0
    num_Independientes = []
    while cont < 3:
        num_random = random.randint(-20,20)
        if num_random != num_Independientes and num_random != b and num_random != 0:
           num_Independientes.append(num_random)
           cont +=1     
    for i in num_Independientes:
        print('y = ' + str(a)+'x + ' + str(i))
        

def rectaPerpendicular2 (a,b):
    cont = 0 
    num_CoeficienteP= []
    
    while cont < 3: 
        num_random = random.randint(-20,20)
        if num_random != num_CoeficienteP and num_random != a and num_random != 0 :
            num_CoeficienteP.append(num_random)
            cont += 1
        
    for i in num_CoeficienteP:
   
        pendiente = Fraction(i,random.randint(-20,20))    
        print('Pendiento original : y = ' + str(pendiente) + ' X + ' + str(b))
        cambiando_pendiente = -1 / pendiente
        print('Cambiando la pendiente: y = ' + str(cambiando_pendiente) + ' X + ' + str(b) )

def rectaPerpendicular(a,b):
    cont = 0
    num_Independientes = []
    while cont < 3:
        num_random = random.randint(-20,20)
        if num_random != num_Independientes and num_random != b and num_random != 0:
           num_Independientes.append(num_random)
           cont +=1
    cambiando_pendiente = -1 / a     
    for i in num_Independientes:
        print('y = ' + str(cambiando_pendiente)+'x + ' + str(i))
        
        
        
def recta(a,b):
    # y = ax + b
    # 0 = ax + b
    # x = -b/a

    if a > 0:
        pendiente = 'Creciente'
    elif a < 0:
        pendiente = 'Decreciente'
    else:
        pendiente = 'Horizontal'

    if a != 0:
        x = -b/a
        print('Corte en X = ' + str(x))
    else:
        print('La recta es paralela al eje Y y no tiene corte en X')

    print('Corte en Y = ' + str(b))
    print('Pendiente = ' + str(pendiente))

def parabola(a,b,c):
    
    if (b*b - 4*a*c) < 0:
        
        print("La parábola no tiene soluciones reales.")
        
    elif (b*b - 4*a*c) == 0:
        
        x = -b / (2*a) #Eje de Simetria
        print("La parábola toca el eje x en un solo punto: " + str(x)) #Como el discriminante es 0 se reduce la expresion para calcular la raiz
        
    else:
        
        x1 = Fraction(-b+sqrt(b*b-4*a*c))/(2*a)  # Fórmula de Bhaskara parte positiva
        x2 = Fraction(-b-sqrt(b*b-4*a*c))/(2*a)  # Fórmula de Bhaskara parte negativa
        
        print('Las soluciones de la ecuación son: \n x1= ' + "{0:.2f}".format(float(x1)), ' \n x2= ' + "{0:.2f}".format(float(x2)))
        
    if a>0:
        print ("La parábola es concava hacia arriba")
        print(f"El intervalo de decrecimiento es del infinito hasta {'{0:.2f}'.format(float(-b)/(2*float(a)))},y de crecimiento desde {'{0:.2f}'.format(float(-b)/(2*float(a)))} al Infinito. ")
    elif a<0:
            print ("La parábola en concava hacia abajo")
            print(f"El intervalo de crecimiento es del infinito hasta {'{0:.2f}'.format(float(-b)/(2*float(a)))}, y de decrecimiento desde {'{0:.2f}'.format(float(-b)/(2*float(a)))} al Infinito.")      
    else:
        print("Si 'a' es igual a 0 la función no es cuadratica")            
        print("El corte con el eje 'y' es: ",c )






def sucesion_aritmetica(a, b, c):
    sucesion = []
    for i in range(c):
        termino = a + (i*b)
        sucesion.append(termino)
    if sucesion[i]> a:
        print(f'La sucesion es creciente, el primer termino de la sucesión es: {a}, su diferencia es de: {b} y la sucesión es: ')
        x = 0
        for i in sucesion:
            x += 1
            print(f'valor {x}: {i}')
    else:
        print(f'La sucesion es decreciente, el primer termino de la sucesión es: {a}, su diferencia es de: {b} y la sucesión es: {sucesion}')
        x = 0
        for i in sucesion:
            x += 1
            print(f'valor {x}: {i}')
    

def sucesion_geometrica(a, b, c):
    sucesion = []
    for i in range(c):
        termino = a * (b**i)
        sucesion.append(termino)
    if sucesion[i]> a:
        print(f'La sucesion es creciente, el primer termino de la sucesión es: {a}, su razón es: {b} y la sucesión es: {sucesion}')
        x = 0
        for i in sucesion:
            x += 1
            print(f'valor {x}: {i}')
    else:
        print(f'La sucesion es decreciente, el primer termino de la sucesión es: {a}, su razón es: {b} y la sucesión es: {sucesion}')
        x = 0
        for i in sucesion:
            x += 1
            print(f'valor {x}: {i}')



