# Divisor de Sorvetes
# Entrade de informacoes
print("Quantidade de Sorvete")
qnt_sorvete = int(input())
print("Quantidade de  pessoas")
qnt_pessoas = int(input())

# Inicio do programa

if qnt_sorvete == qnt_pessoas or qnt_sorvete % 2 == 0:
    print("Divida")
else:
    print("Coma Sozinho")