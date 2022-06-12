#Solução elaborada a partir do algoritmo exemplificado no portal 
#https://www.macoratti.net/alg_cnpj.htm#:~:text=Algoritmo%20para%20valida%C3%A7%C3%A3o%20do%20CNPJ&text=O%20n%C3%BAmero%20que%20comp%C3%B5e%20o,que%20s%C3%A3o%20os%20d%C3%ADgitos%20verificadores.

import numpy

def validacaodados_12_digitos():
    while True:
        cnpj_Sem_DV = input('Digite os 12 primeiros digitos do seu CNPJ (RAIZ CNPJ): ')
        print('')
        if not cnpj_Sem_DV.isdecimal() or ((len(str(cnpj_Sem_DV))) != 12) == True:
            print('\033[31mERRO! Valor inválido! Tente Novamente.\n\033[m')
            continue
        else:
            x = list(map(int,cnpj_Sem_DV))
            return x
        
def validacaodados_2_digitos():
    while True:
        cnpj_DV = input('Digite os 2 últimos digitos do seu CNPJ: ')
        print('')
        if not cnpj_DV.isdecimal() or ((len(str(cnpj_DV))) != 2) == True:
            print('\033[31mValor inválido! Tente Novamente.\n\033[m')
            continue
        else:
            x = list(map(int,cnpj_DV))
            return x
        
lista_produto_1_DV = [5,4,3,2,9,8,7,6,5,4,3,2]
lista_produto_2_DV = [6,5,4,3,2,9,8,7,6,5,4,3,2]

loop = True
while True:
    
    cnpjRaiz = validacaodados_12_digitos()
    cnpjDV = validacaodados_2_digitos()
    variavel_de_validacao = cnpjRaiz
   
    restoDivisao_inteira = sum(numpy.multiply(variavel_de_validacao, lista_produto_1_DV))%11
    
    if restoDivisao_inteira == 10:
        calculadoDV_01 = 0
    elif restoDivisao_inteira <= 2:
        calculadoDV_01 = 0
    else:
        calculadoDV_01 = 11-restoDivisao_inteira
        
    variavel_de_validacao.append(calculadoDV_01)
        
    restoDivisao_inteira = sum(numpy.multiply(variavel_de_validacao, lista_produto_2_DV))%11

    if restoDivisao_inteira == 10:
        calculadoDV_02 = 0
    elif restoDivisao_inteira <= 2:
        calculadoDV_02 = 0
    else:
        calculadoDV_02 = 11-restoDivisao_inteira
        
    validacao_DV = [calculadoDV_01, calculadoDV_02]
    
    if cnpjDV == validacao_DV:
        print('CNPJ Validado com sucesso!')
        loop = False
        
    else:
        print('\033[31mCNPJ Não Validado! Tente novamente.\n\033[m')
        continue
    