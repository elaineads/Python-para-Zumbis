texto = 'The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live upto these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'
lista = []
texto = texto.replace('.', '').replace(',', '').replace(':', '')
texto = texto.lower()
texto = texto.split(' ')

for x in texto:
    if x[0] in 'python' or x[-1] in 'python':
        lista.append(x)
        
print(lista)
