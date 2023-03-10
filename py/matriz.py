x = []
m = int(input("m: "))
n = int(input("n: "))

for i in range(m):
  linha = []
  for j in range(n):
    linha.append( input("X%i%i: " % (i, j) ) )
  linha.reverse()
  x.append(linha)

  

for i in range(m):
  for j in range(n):
    print(x[i][j], end = ' ')
  print() 