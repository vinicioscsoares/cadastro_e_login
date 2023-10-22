from controller import ControllerCadastro, ControllerLogin

while True:
  print('==========[MENU]============')
  decidir = int(input('digite 1 para cadastrar \nDigite 2 para Logar \n Digite 3 para sair'))
  
  if decidir == 1:
    nome = input(f'Digite seu nome: ')
    email = input(f'Digite o seu email:')
    senha = input(f'Digite sua senha: ')
    ControllerCadastro.cadastrar(nome, email, senha)
    if ControllerCadastro.cadastrar == 3:
      print('Cadastro feito com sucesso!')
  elif decidir == 2:
    email = input(f'Digite o seu email:')
    senha = input(f'Digite sua senha: ')
    ControllerLogin.login(email, senha)
    if ControllerLogin == True:
      print('Login feito com sucesso!')
    elif ControllerLogin == False:
      print('Alguma coisa deu errado. Por favor, verifique o email e senha')
  else:
    print('saindo!')
  