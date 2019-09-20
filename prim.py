def Prim ():
    global iguales,op,x,marcados, marcados1, padres, m, temp, temp2, minimos, x
    print("Op: "+str(op)+", Iguales: "+str(iguales))
    iguales=False
    while op !=0:
        temp = 99
        print("Padres: "+str(padres))
        print("Minimos: "+str(minimos))
        for i in range(9):
            if padres[i] == 0:
                if m[x][i] != 0 and marcados[i] != 1:
                    if minimos[i] > m[x][i]:
                        minimos[i] = m[x][i]
                        padres[i] = x+1
                    if m[x][i] < temp:
                        temp = m[x][i]
                        temp2 = i
                        print("break")
                        break
        x = temp2
        print
        print(marcados1)
        print
        if marcados[temp2]==0:
            marcados[temp2] = 1
        else:
            marcados[temp2]=2
            
        '''
    
        '''
        print
        print(marcados1)
        print
        print(marcados)
        print
        print(padres)
        print
        
        for i in range (9):
            if(marcados[i]==marcados1[i]):
                iguales=True
            else:
                iguales=False
                break
        
        
        op = 0
        for i in range(9):
            if marcados[i] == 0 and iguales==False:
                op = 1    
        marcados1=list(marcados)
        
    return iguales

print("PROGRAMA ALGORITMO DE PRIM")
print

padres = [0]*9
marcados = [0]*9
minimos = [99]*9
m = [0]*9

for i in range(9):
    m[i]=[0]*9

m[0][2] = 1
m[0][8] = 4
m[1][8] = 1
m[2][0] = 1
m[2][3] = 3
m[2][4] = 1
m[2][8] = 5
m[3][2] = 3
m[3][4] = 4
m[4][2] = 1
m[4][3] = 4
m[4][5] = 6
m[4][6] = 7
m[5][4] = 6
m[5][6] = 4
m[6][4] = 7
m[6][5] = 4
m[6][7] = 3
m[6][8] = 2
m[7][6] = 3
m[7][8] = 7
m[8][0] = 4
m[8][1] = 1
m[8][2] = 5
m[8][6] = 2
m[8][7] = 7

x=0;  op=1; marcados[0]=1; minimos[0]=0; marcados1=list(marcados); iguales=False



for i in m:
    print(i)
'''
while op !=0:
    temp = 99
    for i in range(9):
        if padres[i] == 0:
            if m[x][i] != 0 and marcados[i] != 1:
                if minimos[i] > m[x][i]:
                    minimos[i] = m[x][i]
                    padres[i] = x+1
                if m[x][i] < temp:
                    temp = m[x][i]
                    temp2 = i
    x = temp2
    print()
    print(marcados1)
    print()
    if marcados[temp2]==0:
        marcados[temp2] = 1
    else:
        marcados[temp2]=2
        
    print()
    print(marcados1)
    print()
    print(marcados)
    print()
    print(padres)
    print()
    
    for i in range (9):
        if(marcados[i]==marcados1[i]):
            iguales=True
        else:
            iguales=False
            break
    
    print("Iguales: "+str(iguales))
    
    op = 0
    for i in range(9):
        if marcados[i] == 0 and iguales==False:
            op = 1    
    marcados1=list(marcados)
    print("Op: "+str(op))
    '''
while(Prim()):
    minimos1=[99]*9
    for i in range (9):
        menor=100
        for j in range (9):
            if m[i][j]<menor and m[i][j]!=0:
                menor=m[i][j]
        minimos1[i]=menor
        
    for i in range (9):
        if marcados[i] >1:
            for j in range (9):
                if m[i][j] == minimos1[i] and padres[j]!=i+1:
                    padres[i]=j+1
                    marcados[i] = 1
                    marcados[x]=1
                    break
            break
    print
    print("Correccion: "+str(marcados))
    print
    print("Padres: "+str(padres))
                
print("Marcados final: "+str(marcados))
print
print("Padres final: "+str(padres))
print
    
for i in m:
    print(i)