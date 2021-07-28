## 1

# print(2 + 2 < 4)

# ## 2

# print( 7 // 3 == 1 + 1 )

## 3

# print(3**2 + 4**2 == 25)

## 4

# print(2+4+6 > 12)

## 5

# print(1387&19 == 0 )

## 6

# print(31%2 == 0)

## 7

# print(min(34,29,31) < 30)

## 8

# if(age > 60):
#   print("Você tem direito aos benefícios")

## 9

# if(damage > 10 and shield == 0):
#   print("Você está morto")

## 10

# if(norte or sul or leste or oeste):
#   print("Você escapou")


      ### Condicional Composta

##  1

# if(ano%4 == 0):
#   print("Ano bissexto")
# else:
#   print("Não é ano bissexto")

## 2

# if(cima and baixo): 
#   print("Decida-se!")
# else:
#   print("Você escolheu um caminho!")

      ### Exercicio

## 1

# l1 = int(input("Digite o valor do primeiro lado"))
# l2 = int(input("Digite o valor do segundo lado"))
# l3 = int(input("Digite o valor do terceiro lado"))

# if(l1 and l2 and l3 > 0):
#   if((l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1)):
#     if(l1 == l2 and l3):
#       print("Equilatero")
#     elif(l1 != l2 and l1 != l3 and l2 != l3):
#       print("Escaleno")
#     else:
#       print("Triango Isóceles")
#   else:
#     print("Os valores n servem pra formar um triangulo")
# else:
#   print("Não podemos ter lados iguais a 0")

## 2

# print("1 - Adição")
# print("2 - Subtração")
# print("3 - Multiplicação")
# print("4 - Divisão")

# op = int(input("Qual operação deseja? "))
# valor1 = int(input("Digite o primeiro valor: "))
# valor2 = int(input("Digite o segundo valor: "))

# if(op == 1):
#   result = valor1 + valor2
#   print("O resultado da soma é: {} ".format(result))
# elif(op == 2):
#   result = valor1 - valor2
#   print("O resultado da subtração é: {} ".format(result))
# elif(op == 3):
#   result = valor1 * valor2
#   print("O resultado da multiplicação é: {} ".format(result))
# elif(op == 4):
#   result = valor1 / valor2
#   print("O resultado da divisão é: {} ".format(result))
# else: ]
#   print("Operação invalida")

## 3 

kwh = int(input("Quantidade de kWh consumido: "))
print(" ")
print("R - Residêncial")
print("I - Insdustrial")
print("C - Comercial")
print(" ")
type = input("Digite seu tipo de instalação: ")

if(type == 'R' or type == 'I' or type == 'C'):

  if(type == 'R'):
    if(kwh <= 500):
      total = kwh * 0.40 
      print("Preço total: {} ".format(total))
    else:
      total = kwh * 0.65
      print("Preço total: {} ".format(total))

  elif(type == 'I'):
    if(kwh <= 100):
      total = kwh * 0.55 
      print("Preço total: {} ".format(total))
    else:
      if(kwh >= 1000):
        total = kwh * 0.60
        print("Preço total: {} ".format(total))
  else:
    if(kwh <= 5000):
      total = kwh * 0.55
      print("Preço total: {} ".format(total))
    else:
      total = kwh * 0.60
      print("Preço total: {} ".format(total))
else:
  print("Operação invalida")
