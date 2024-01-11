# Criando um retângulo - Meu jeito
for i in range (0,3):
  print('*', end=' ')
  for j in range(0,4):
    print('*', end = ' ')
    if j == 3:
      print('')
      

# Resolução 
largura=5
altura = 3
for col in range (altura):
  for j in range(largura):
    print('*', end= ' ')
  print() # Avanca para a próxima linha
