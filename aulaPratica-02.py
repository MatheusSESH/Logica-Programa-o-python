############### Letra A: 

a = 1 + 2 + 3 + 4 + 5

print("A soma dos 5 primeiros numeros inteiros positivos é: {} " .format(a))


############### Letra B:

soma = 23 + 19 + 31

media = soma/3

print("A media entre 23, 19 e 31 é: {} " .format(media))


############### Letra C:

result = 403 // 73

print("A quantidade de vezes que 73 cabe em 403 é: {} " .format(result))


############### Letra D: 

result = 403 % 73

print("A sobra da divisão entre 403 por 73 é: {} ".format(result))


############### Letra E: 

result = 2**10

print("2 na potência de 10 é: {} " .format(result))


############### Letra F:

result = abs(54 - 57)

print("O valor absoluto entre 54 e 57 é: {} " .format(result))


############### Letra G:

result = min(34, 29, 31)

print("O valor minimo entre 34, 29 e 31 e 31 é: {} " .format(result))


############################# ATRIBUIÇÃO ################################

a = 3

b = 4

c = a*a + b*b



############################# STRINGS ################################

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

############### Letra A:

a = s1+ ' ' +s2+ ' ' +s3

print(a)

############### Letra B:

print((s1 + ' ')*10)

############### Letra C:

print(s1+ ' ' + (s2 + ' ') * 2 + (s3 + ' ' ) * 3)

############### Letra D:

print((s1 + ' ' + s2 + ' ')*10)

############### Letra E:

print(((s2)* 2 +s3+ ' ')*5)


############################# EXERCICIOS ################################

############### 1: 

produto = float(input("Digite o valor do produto: $ "))

desconto  = float(input("Digite o valor do desconto: "))

valor = produto * (desconto / 100)
valorF = produto - valor

print("O valor do produto final é: ${} " .format(valorF))


############### 2:

percorrido = int(input("Quantidade de KM percorridos: "))
dias_alugados = int(input("Dias alugados: "))

aluguelKM = 0.15 * percorrido
aluguelDias = 60 * dias_alugados

valorFinal = aluguelKM + aluguelDias

print("Valor total do aluguel é: {} " .format(valorFinal))


############### 3:

frase = input("Digite uma frase: ")

frase = frase.replace(" ", "")

print(frase)

tamanhoFrase = len(frase)

novaFrase = frase[:int(tamanhoFrase/2)]

print(novaFrase[-2:])