# Condicional simples: 

v1 = int(input("Digite um valor: "));
v2 = int(input("Digite outro valor: "));

if(v1 > v2):
  print("O primeiro valor é maior que o segundo"); 

# Condicional Composta: 

v1 = int(input("Digite um valor: "))

if(v1%2 == 0):
  print("O valor é par")
else:
  print("O valor é impar")

# Expressões logicas

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

result = (n1 >= 7) and (n2 >= 7) and (n3 >= 7)

if(result):
  print("Aprovado!")
else: 
  print("Reprovado")

# Condicionais aninhadas 

print("1 - Maça")
print("2 - Laranja")
print("3 - Banana")
print(" ")

product = int(input("O que deseja comprar? "))
quant = int(input("Quantas unidades? "))

if(product == 1): 
  total = quant * 2.30
  print("O valor total é {} ".format(total))
else: 
  if(product == 2):
    total = quant * 3.60
    print("O valor total é {} ".format(total))
  else:
    if(product == 3):
      total = quant * 1.85
      print("O valor total é {} ".format(total))
    else:
      print("Produto inexistente!")