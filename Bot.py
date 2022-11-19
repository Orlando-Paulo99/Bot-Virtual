

def assunto():
	print("Olá,Seja bem-vindo(a) ao meu mundo")
	name=input("Qual o seu nome? ")
	print(f"{name} obrigado por chegar até aqui")
	idade=int(input("Qual a sua idade? "))
	if idade < 18:
		print("Vixee,você tá no leitinho ainda")
		
	email=input("Digite seu  email ")
		
	resposta=input(f"{name} o que gostaria de saber sobre mim? \nDigite-1 para saber meu nome completo \nDigite-2 para saber minha idade \nDigite-3 para saber meu cpf \nDigite-4 para saber onde eu moro")
	
def respondendo(resposta,name):
		if resposta ==1:
			print("Orlando Paulo de Hermogenes Filho")
		elif resposta ==2:
			print(f"Tenho 22 anos, {name},algum problema?")
		elif resposta == 3:
			print(f"{name},vai procurar um trouxa kkkkkkk")
		
		elif resposta==4:
			print("Quase no céu")
		

		
		


assunto()
respondendo(resposta,name)		
	
