código_do_produto = int(input("digite o código do produto:" ))
quantidade = int(input("digite a quantidade do produto:"))
#entradas das variantes::

if código_do_produto == 1: #comandos de decisão 
    if quantidade >= 32:
        print("arroz comprado com valor total de R$ {:.2f},tendo desconto".format((quantidade * 3,20) - (quantidade * 3,20) * 15/100)) 
    else:
        print("arroz comprado com valor total de R${:.2f} ,".format(quantidade * 3,20))
elif código_do_produto == 2:
     if quantidade >= 25:
         print("feijão comprado com valor total de R$ {:.2f}, tendo desconto".format((quantidade * 4,00) - (quantidade * 4,00) * 15/100))
     else:
         print("feijão comprado com valor total de R$ {:.2f},".format(quantidade * 4,00))
elif código_do_produto == 3:
     if quantidade >= 4:
         print("carne comprada com valor total de R$ {:.2f}, tendo desconto".format((quantidade * 30,00) - (quantidade * 30,00) * 15/100))
     else:
         print("carne comprada com valor total de R${:.2f} ".format(quantidade * 30,00))
elif código_do_produto == 4:
     if quantidade >= 23:
        print("leite comprado com valor total de R$ {:.2f}, tendo desconto".format((quantidade * 4,50) - (quantidade * 4,50) *15/100))
     else:
        print("leite comprado com valor total de R${:.2f},".format(quantidade * 4, 50))