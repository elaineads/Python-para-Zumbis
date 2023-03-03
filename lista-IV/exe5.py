texto = 'The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live upto these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'
lista = []
texto = texto.replace('.', '').replace(',', '').replace(':', '')
texto = texto.lower()
texto = texto.split(' ')

def valida(palavra):
    for letra in palavra:
        if letra in 'python':
            return True
    return False

lista = []
for x in texto:
    if valida(x) and len(x) > 4:
        lista.append(x)
        
print(lista)

