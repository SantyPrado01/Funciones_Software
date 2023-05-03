import random
from fractions import Fraction

def rectaParalela(a,b):
    cont = 0
    num_Independientes = []
    while cont < 3:
        num_random = random.randint(-20,20)
        if num_random != num_Independientes and num_random != b:
           num_Independientes.append(num_random)
           cont +=1     
    for i in num_Independientes:
        print('y = ' + str(a)+'x + ' + str(i))
        

def rectaPerpendicular (a,b):
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



def recta(a,b):
    if a > 0:
        pendiente = 'Creciente'
    else:
        pendiente = 'Decreciente'

    raiz = (a * -1 ) / b
    print('Corte en X = ' + str(raiz))
    print('Corte en Y = ' + str(a))
    print('Pendiente = ' + str(pendiente))
    