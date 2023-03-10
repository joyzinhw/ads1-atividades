def string(nome,espaço):
 for i in range(len(nome)-1): 
  if i == (len(nome) - 2):
   espaço += nome[i] + " "
  else: 
   espaço += nome[i] + " "
  print(f"{nome[-1].upper()},{espaço}")

string(nome = input("Digite o seu nome: ").split(" "), espaço = " ")