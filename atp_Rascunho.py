# ATP Raciocinio Logico                         #
# Aluno: Michael Nicholas O. Castilho           #
# Prof/Tutor: Lucas Emanuel Silva E Oliveira    #
# Turma: 11100010563_20211_02                   #
#################################################

# CADASTRO PARA OBTER INFORMACOES PESSOAIS #

def obter_limite():
      
      from time import sleep

      nome_cliente=  input('Nome Completo: ')
      
      nome = ('Michael Nicholas')
      
      sobrenome = ('Oliveira de Castilho')
      
      cargo = input('Informe sua FUNCAO : ')
      
      salario = float(input('Informe seu SALARIO : '))
      
      data_nasc= input('Informe sua DATA DE NASCIMENTO : ')

      ano_nasc = int(data_nasc.split('/')[2])


# IMPORTAR DATA #

      from datetime import date
      data = date.today()
      ano = int(data.strftime ('%Y'))
      anos = ano - ano_nasc
      limite = (salario * (anos/1.000)+100)
      
# PRINTAR INFORMACOES #

      print ('Aguarde um momento !!!')

      sleep (4)

      print (10*'- - ')
      print (10*'- - ')
      print (10*'- - ')
      
      
      print ('{}\nTrabalha como : {}\nSeu salario de: R$: {:0.2f}  por mês \nNasceu no ano de {}'.format(nome_cliente,cargo,salario,ano_nasc))

      print('{} Anos'.format(anos))
      
      correto= input('Correto ? \nPressione (S) para SIM \n\t  (N) para NAO\n').upper()
      
# VERIFICAR INFORMACOES #

      if correto == 'N':
            
            print(10*'- - ')
            
            return obter_limite()
      
      elif correto == 'S':

            sleep(1)
            
            print (10*'- - ')
            print ('Voce Tem um total de R$:{:0.2f} em CREDITO com a loja.\n'.format(limite))
            print (10*'- - ')
            
            print()
            

            return nome,sobrenome,limite,anos
            
      
# VERIFICADOR DE PRODUTO #

def verificar_produto(valor_produto, limite, desconto1,n1):

      from time import sleep

      if valor_produto <= limite * 0.6:

            print('Compra Liberada !!!')

            sleep(2)

            if valor_produto <= desconto1 and (valor_produto - n1) != 0:
            
                  print('voce tem um desconto de {}% no produto'.format(n1))

                  sleep(1)

                  print('valor  {} sem Desconto:{}\nValor do {} Com Desconto: {}'.format(produto, valor_produto, produto, abs(valor_produto-n1)))

                  sleep(1)

      elif valor_produto >= limite * 0.6 and valor_produto < limite * 0.9:

            print('Compra Liberada somente com o parcelamento em ate 2 vezes !!!')

            sleep(2)

            if valor_produto <= desconto1 and (valor_produto - n1) != 0:

                  print('voce tem um desconto de {}% no produto'.format(n1))

                  sleep(1)

                  print('valor  {} sem Desconto:{}\nValor do {} Com Desconto: {}'.format(produto, valor_produto, produto, abs(valor_produto-n1)))

                  sleep(1)

      elif valor_produto >= limite * 0.9 and valor_produto <= limite:

            print('Compra Liberada somente com o parcelamento de 3 ou mais vezes !!! ')

            sleep(2)

            if valor_produto <= desconto1 and (valor_produto - n1) != 0:

                  print('voce tem um desconto de {}% no produto'.format(n1))

                  sleep(2)

                  print('valor  {} sem Desconto:{}\nValor do {} Com Desconto: {}'.format(produto, valor_produto, produto, abs(valor_produto-n1)))

      else:

            print('Compra NEGADA !!! *** Por ultrapassar seu LIMITE DE CREDITO *** ')

          


# VERIFICADOR DE DESCONTO #

def desconto(nome,sobrenome,anos):

      n1 = len(nome)
      n2 = len(sobrenome)
      desconto1 = n1+n2+anos

      return desconto1,n1
      


print ('-------------------------------------------------------------')
print ('-------------- BEM-VINDO A INFOPYTHON -----------------------')
print ('------------- A SUA LOJA DE INFORMATICA ---------------------')
print ('-------------------------------------------------------------\n')


print ('******** ANALISE DE CREDITO ********\n')


input('Pressione ENTER para continuar!!')


# VARIAVEIS GLOBAL #

nome,sobrenome,limite,anos = obter_limite()

print (10*'- - ')
print (10*'- - ')
print (10*'- - ',end='\n')

numero_produto= int(input('Por gentileza ,digite a quantia de produtos  que deseja cadastrar:'))

quantia= 1

soma= limite

valor_limite= soma

desconto1,n1= desconto(nome,sobrenome,anos)


# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=- #

####################
# INICIO DO CODIGO #
####################


## ESTRUTURA DE REPETICAO ##

while quantia <= numero_produto:
      
      if (valor_limite) <= (0):

            print('Voce Chegou ao  valor total do limite de credito')

            break
      
      print(' ======================')
      print(' ===Produto Numero {0}==='.format(quantia))
      print(' ======================\n')
      
      produto = input('Nome Produto: ')
      
      valor_produto= float(input('Valor Produto: '))
      
      print('{} Custa R$:{}'.format(produto,valor_produto))

      
      quantia+=1

      valor_limite-=valor_produto
            
      
      if (valor_limite)> 0 :

            print('Voce possui R$:{} em creditos\n'.format(valor_limite))

      
      
      verificar_produto(valor_produto, limite, desconto1,n1)

print('Obrigado, Por comprar Com a Gente !')      

exit()


