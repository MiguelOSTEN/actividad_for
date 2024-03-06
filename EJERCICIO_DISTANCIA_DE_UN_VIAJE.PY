import os
os.system ('cls')

kilometrosint = 0
totalkmint = 0
etapaint =int(input('Cuantas paradas va ralizar ---->'))
for i in range(etapaint):
    var_etapaint =int(input('Ingrese los km recorridos en el trayecto----------->'))
    totalkmint += var_etapaint
    
print('Etapas recorridas:',etapaint)
print(totalkmint,'KM Recorridos ')   


enter= input('\n<Salir del programa')
