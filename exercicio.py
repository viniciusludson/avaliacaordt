#criar uma função que recebe duas strings que serão convertidas para números para serem somadas se ao realizar o casting ocorrer um erro, gere uma exceção informando o motivo
#fazendo tratamento de erro com except
'''def soma(str1, str2):
    try:
        num1= float(str1)
        num2= float(str2)
        return num1 +num2

    except:
        raise Exception(" Falha ao transformar em string. O valor não pode ser convertido! ")
print(soma("1", '2'))


#crie uma função que receba que receba uma lista e um número e retorne o elemento da lista na posição deste número.
# Faça um tratamento de erro para que caso haja um acesso fora do indice a função retorne o valor None'''
def retornar(lista, indice):
    try:
        return lista[indice]
    except:
        return print("Falha ao retornar o valor! ")
lista=[34, 67,12, 39, 32, "A"]
print(retornar(lista, 5))

#para ver o tratamento de erro, usa um indice que não tem na lista
