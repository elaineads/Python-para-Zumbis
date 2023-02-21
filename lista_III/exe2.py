usuario = input('Usuário: ')
senha = input('Senha: ')

while usuario == senha:
    print('Usuário e senha não podem ser iguais.')
    usuario = input('Usuário: ')
    senha = input('Senha: ')
