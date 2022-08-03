#Cicle
while True:

#Import mod regex
    import re

#Header
    print ("------------------------------------------------------------------------------------------------")
    print ("---------------------------------------Payroll SYSTEM.exe---------------------------------------")
    print ("------------------------------------------------------------------------------------------------")

#Input data
    while True:
        try:
            iD=int(input("Digite su número de documento (Solo números, sin caracteres especiales como puntos): "))
            re.match("^\d{8,10}$", iD)
            if TypeError:
                print ("Naisn´t")
            else:
                print ("Nais")
        except ValueError:
            print ("------------------------------------------------------------------------------------")
            print ("Error: Debe digitar caracteres numéricos")
        else:
            break
    while True:
        try:
            name=str(input("Digite sus nombres y apellidos: "))
        except ValueError:
            print ("------------------------------------------------------------------------------------")
            print ("Error: Debe digitar caracteres alfabéticos")
        else:
            break
    while True:
        try:
            salary=float(input("Digite el valor de su salario mensual: $"))
        except ValueError:
            print ("------------------------------------------------------------------------------------")
            print ("Error: Debe digitar caracteres numéricos")
        else:
            break
    while True:
        try:
            days=int(input("Digite el total de días trabajados en el mes: "))
        except ValueError:
            print ("------------------------------------------------------------------------------------")
            print ("Error: Debe digitar caracteres alfabéticos")
        else:
            break
    while True:
        dependient=str(input('¿Es usted trabajador dependiente? (Responda con "Si" o "No"): '))
        if dependient=="Si" or dependient=="No":
            break
        else:
            print ("------------------------------------------------------------------------------------")
            print ('Error, debe ingresar únicamente uno de los valores indicados ("Si" o "No")')

#Operations
    sTransport=117120
    healthPension=float
    if salary>2000000:
        sTransport=0
    if dependient=="Si":
        healthPension=0.08
    else:
        healthPension=0.2
    if salary>4000000:
        healthPension=healthPension+0.01    
    totalSalary=((salary+sTransport-(healthPension*salary))/30)*days

#Result
    print ("Señor(a)",name,", identificado con el número de documento",iD,". Su pago según los datos ingresados (salario, dias, y si es empleado dependiente o no) es de: $",totalSalary,".")
    print ("------------------------------------------------------------------------------------")

#Continue
    while True:
        continu=str(input('¿Desea continuar consultando nóminas? (Responda con "Si" o "No"): '))
        if continu=="Si" or continu=="No":
            break
        else:
            print ("------------------------------------------------------------------------------------")
            print ('Error, debe ingresar únicamente uno de los valores indicados ("Si" o "No")')
    if continu=="No":
        break

#Failed code
'''
patronID=int
patronID.findall(r'\d{8, 10}\d', iD)
patronID.findall(iD)
if iD==patronID.findall:
break
else:
print ("Error: La cadena de caracteres debe ser de 8 a 10")
'''