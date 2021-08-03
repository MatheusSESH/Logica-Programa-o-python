# Estrutura de repetição For

# valor = 0
# qtd = 0
# for x in range(1,101):
#   if( x % 2 == 0 ):
#     valor += x
#     qtd += 1

# media = valor/qtd
# print(media)

# Estrutura de repetição aninhada

xw = 1
while( xw < 11 ):
  xf = 0
  for xf in range(1,11):
    total = xw * xf
    print("{} * {} = {}" .format(xw,xf,total))
  print(" ")
  xw += 1