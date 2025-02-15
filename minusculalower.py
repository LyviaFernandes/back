letra = str(input('Insira uma letra: ')).lower() # Garantido letra minuscula

if letra in 'a,e,i,o,u':
    print('É uma vogal')
else:
    print('É consoante')
