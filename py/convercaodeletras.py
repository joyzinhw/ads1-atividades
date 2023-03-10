from string import digits

palavra= input("Digite algo:").strip( )
numero = str.maketrans(' ' , ' ', digits)
outra_palavra = palavra.translate(numero)

consoantes = "bcdfghjklmnpqrstvwxz - BCDFGHJKLMNPQRSTVWXZ"

vogais = "aeiou - AEIOU"

for letra in palavra:
	if letra in vogais:
		print(letra.upper( ))
	elif letra in consoantes:
		print(letra)