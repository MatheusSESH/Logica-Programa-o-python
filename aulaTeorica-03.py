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