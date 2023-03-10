numero = int(input('digite um número positivo:'))
#entrada das variantes 

adição = 0
divisores = []

#comando de repetição que vai rodar o input 
for j in range(numero -1):  
  divisão = numero/ (j+1)
  if divisão //1 == divisão:
     divisores.append(j + 1)
     adição = sum(divisores)  
#sum vai realizar a soma dos itens 

if adição == numero:  
   divisores.reverse()  
  #reverse é usando para inverter a ordem dos itens
   print(adição, end="=")

   for j in divisores:
      if j == divisores[len(divisores)-1]:
         print(j, end=" ") 
      else:
         print(j, end="+" ) 

elif adição != numero:
   print('este número não é perfeito')
 