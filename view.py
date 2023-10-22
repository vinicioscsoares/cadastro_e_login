from controller import ControllerCadastro, ControllerLogin

while True:
  print('==========[MENU]============')
  decidir = int(input('digite 1 para cadastrar \nDigite 2 para Logar \n Digite 3 para sair'))
  
  if decidir == 1:
    nome = input(f'Digite seu nome: ')
    email = input(f'Digite o seu email:')
    senha = input(f'Digite sua senha: ')
    resultado = ControllerCadastro.cadastrar(nome, email, senha)
    if resultado  == 2:
      print('Tamanho do nome inválido')
    elif resultado == 3:
      print('email maior que 200 caracteres')
    elif resultado == 4:
      print('tamanho da senha inválido')
    elif resultado == 5:
      print('Email já cadastrado')
    elif resultado == 6:
      print('Erro interno no sitema')
    elif resultado == 1:
      print('Cadastro realizado com sucesso!')
    
  elif decidir == 2:
    email = input(f'Digite o seu email:')
    senha = input(f'Digite sua senha: ')
    resultado = ControllerLogin.login(email, senha)
    if not resultado:
      print('Email ou senha inválidos!')
    else:
      print(resultado)
    
    
  else:
    break
  