def imprimirnome(nome):
    print(nome)

def piramide(t):
    for x in range (1,t+1,1):
        for y in range (0,x):
            print(x,end="")
        print()

def vogal(texto):
    contador=0
    vogais="aeiou"
    for x in range (len(texto)):
        if texto[x] in vogais:
                contador+=1
    print(contador)

def vogal2(texto):
    contador=0
    for x in range (len(texto)):
        if texto[x]=="a" or texto[x]=="e" or texto[x]=="i" or texto[x]=="o" or texto[x]=="u":
                contador+=1
    print(contador)

def calculo( produto ,quantp , valorp):
    total=quantp*valorp
    return produto,total

def cal(numero):
    resp="z"
    if numero>0:
        resp="p"
    elif numero<0:
        resp="n"
    return resp

def somar(numero1,numero2):
    valor= numero1+numero2
    print(valor)

def somar(*num):
    soma=0
    for x in range (len(num)):
        soma= soma+ num[x]
    print(soma)


