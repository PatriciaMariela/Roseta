from datetime import datetime
fechaActual = datetime.now()


def extractorFechaALista(): 
    """Se obtienen los valores de las variables día, mes y año"""
    dia = datetime.strftime(fechaActual,"%d")  
    mes = datetime.strftime(fechaActual,"%m")
    anio = datetime.strftime(fechaActual,"%Y")

    listDay=[]

    for x in range(2):
        listDay.append(int(str(dia)[x]))
    for x in range(2):
        listDay.append(int(str(mes)[x]))
    for x in range(4):
        listDay.append(int(str(anio)[x]))
    return listDay

listA = extractorFechaALista() 

def primerSuma():
    
    primerSuma=[]
    for x in range(7):
        """Se suman los 8 valores de la primer lista generando otra lista nueva"""
        suma = listA[x]+listA[x+1]
        if suma <= 9:
            primerSuma.append(suma)
        elif suma > 9:
                """Si la suma es 10 o mayor, se guarda el valor derecho del str, en el ejemplo del 10 se guarda el valor 0, 
                si fuera un 12 se guardará un 2"""
                primerSuma.append(int(str(suma)[1]))                   
    return primerSuma
    
listB= primerSuma()

def segundaSuma():
    segundaSuma=[]
    for x in range(6):
        suma = listB[x]+listB[x+1]
        if suma <= 9:
            segundaSuma.append(suma)
        elif suma > 9:
                segundaSuma.append(int(str(suma)[1]))                   
    return segundaSuma

listC = segundaSuma()


def terceraSuma():
    terceraSuma=[]
    for x in range(5):
        suma = listC[x]+listC[x+1]
        if suma <= 9:
            terceraSuma.append(suma)
        elif suma > 9:
                terceraSuma.append(int(str(suma)[1]))        
    return terceraSuma

listD = terceraSuma()


def cuartaSuma():
    cuartaSuma=[]
    for x in range(4):
        suma = listD[x]+listD[x+1]
        if suma <= 9:
            cuartaSuma.append(suma)
        elif suma > 9:
                cuartaSuma.append(int(str(suma)[1]))        
    return cuartaSuma

listE = cuartaSuma()


def quintaSuma():
    quintaSuma=[]
    for x in range(3):
        suma = listE[x]+listE[x+1]
        if suma <= 9:
            quintaSuma.append(suma)
        elif suma > 9:
                quintaSuma.append(int(str(suma)[1]))        
    return quintaSuma

listF = quintaSuma()


def sextaSuma():
    sextaSuma=[]
    for x in range(2):
        suma = listF[x]+listF[x+1]
        if suma <= 9:
            sextaSuma.append(suma)
        elif suma > 9:
                sextaSuma.append(int(str(suma)[1]))        
    return sextaSuma

listG = sextaSuma()


def septimaSuma():
    septimaSuma=[]
    for x in range(1):
        suma = listG[x]+listG[x+1]
        if suma <= 9:
            septimaSuma.append(suma)
        elif suma > 9:
                septimaSuma.append(int(str(suma)[1]))        
    return septimaSuma

listH = septimaSuma()

def cuaternoA():
     cuateA=[]

     posA=listH[0]+listG[0]     
     posB=listH[0]
     posC=listH[0]+listG[1]
     posD=posA+posC

     if posA <= 9:
            cuateA.append(posA)
     else: cuateA.append(int(str(posA)[1]))
    
     if posB <= 9:
            cuateA.append(posB)
     else: cuateA.append(int(str(posB)[1]))
     if posC <= 9:
            cuateA.append(posC)
     else: cuateA.append(int(str(posC)[1]))
     if posD <= 9:
            cuateA.append(posD)
     else: cuateA.append(int(str(posD)[1]))
     return cuateA  

def cuaternoB():
     cuateAA=cuaternoA()
     cuateB=[]

     posA=cuateAA[0] + cuateAA[1]    
     posB=cuateAA[1] + cuateAA[2]
     posC=cuateAA[2] + cuateAA[3]
     posD=cuateAA[3] + cuateAA[0]


     if posA <= 9:
            cuateB.append(posA)
     else: cuateB.append(int(str(posA)[1]))    
     if posB <= 9:
            cuateB.append(posB)
     else: cuateB.append(int(str(posB)[1]))
     if posC <= 9:
            cuateB.append(posC)
     else: cuateB.append(int(str(posC)[1]))
     if posD <= 9:
            cuateB.append(posD)
     else: cuateB.append(int(str(posD)[1]))

     return cuateB

cuate1=str(cuaternoA())
cuate2=str(cuaternoB())

print("Primer Cuaterno:" + cuate1)
print("Segundo Cuaterno:" + cuate2)