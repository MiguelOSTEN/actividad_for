import os
os.system ( 'cls' ) 

riego_papaint = 3
riego_yucaint = 1
riego_zanahoriaint =2 
totalint = 0

opcionint = int(input('Menu de cultivo \n1.Papa\n2.Yuca\n3.Zanahoria'))

if opcionint ==1:
    print('La cantidad de veces que se va regar en la semana----------->', riego_papaint)
    for i in range(riego_papaint):
        var_litrosint =int(input('Ingrese los litros a regar----------->'))
        totalint += var_litrosint
    print('Litros aplicados en el cultivo--------------->',totalint,'Litros')   
    print('Cantidad de veces que se rego el cultivo de papa  en la semana ---------->',riego_papaint)


if opcionint ==2:
    print('La cantidad de veces que se va regar en la semana----------->',riego_yucaint)
    for i in range(riego_yucaint):
        var_litrosint =int(input('Ingrese los litros a regar '))
        totalint += var_litrosint
    print('Litros aplicados en el cultivo--------------->',totalint)   
    print('Cantidad de veces que se rego el cultivo de yuca  en la semana---------->',riego_yucaint)
    
if opcionint ==3:
    print('La cantidad de veces que se va regar en la semana----------->',riego_zanahoriaint)
    for i in range(riego_zanahoriaint):
        var_litrosint =int(input('Ingrese los litros a regar '))
        totalint += var_litrosint
    print('Litros aplicados en el cultivo--------------->',totalint)   
    print('Cantidad de veces que se rego el cultivo de zanahoria  en la semana---------->',riego_zanahoriaint)