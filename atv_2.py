#1 receber uma string e contar os caracteres
'''frase=input("Digite uma frase: ")
contar=0
for x in frase:
    if x != " ":
        contar+=1
print(f"A frase tem a quantidade de caracteres: {contar}")
#2 questao calculo fatorial sendo recebido pelo input
numero=int(input("Digite um número para calcular o seu fatorial: "))
fatorial=1
if numero<0:
    print("O número é negativo! ")
elif numero==0 or numero==1:
        print(f"O fatorial de {numero} é 1")
        fatorial+=1
else:
    for x in range(numero,1,-1):
        fatorial=fatorial*x
print(f"O fatorial de {numero} é {fatorial}")
#3 questao programa que ler uma quantidade de caracteres e concatene em uma variavel

# 1. Inicializa a variável acumuladora
concatenar = ""
print("Digite algo que queira guardar:  (Não digite nada se quiser apenas parar!, com ENTER )")
while True:
    texto_digitado = input("Digite um texto para armazenar: ")
    if texto_digitado == "":
        break
    concatenar += texto_digitado + " "

print("*" *30,  "*" *30)
print(" -----------Mensagens------------")
print("Junção de textos  concatenados:")
print(concatenar.strip())  #para remover os espaços
#4 questao ler textos e dizer quantas vogais tem no texto
nome=input("Digite um nome ou frase: ")
vogal=input("Digite uma vogal: ")
for i in range(0,len(nome)):
    if vogal==nome[i]:
        print("Encontrei a vogal {} na posição {}".format(vogal,i))
#5 questao verificar se uma letra faz parte de um nome e quantas vez aparece
nome=input("Digite um nome: ")
while(True):
    letra=input("Digite uma letra: ")
    if len(letra) !=1:
        print("Digite apenas uma letra por favor! ")
    else:
        for i in range(0, len(nome)):
            if letra== nome[i]:
                print(f"Encontrei a letra {letra} na posição {i}")
        #break
#6 questao tabuada da divisao de um numero lido pelo input
for x in range(1,11):
    try:
        num1 = float(input("Digite o dividendo: "))
        num2 = float(input("Digite o divisor: "))
    except ValueError:
        print("Erro: Por favor, digite apenas números.")
    if num2 == 0:
        print("Erro: Divisão por zero não é permitida.")
    else:
        resultado = num1 / num2
        print(f"{num1} / {num2} = {resultado}")'''
#7 questao
num=int(input("Digite um número: "))
soma=0
media=0
for i in range(num+1):
    soma=num+1
    media=float(soma/num)
print(soma)
print(media)