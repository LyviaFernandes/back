total = 0
vfeijao = 5.5
varroz = 4
vmacarrao = 2

produto = input('DIgite o código do primeiro produto: ')

if produto == 'feijao':
    total += vfeijao 
elif produto == 'arroz':
    total += varroz
elif produto == 'macarrao':
    total += vmacarrao

produto2 = input('DIgite o código do primeiro produto: ')

if produto2 == 'feijao':
    total += vfeijao 
elif produto2 == 'arroz':
    total += varroz
elif produto2 == 'macarrao':
    total += vmacarrao

produto3 = input('DIgite o código do primeiro produto: ')

if produto3 == 'feijao':
    total += vfeijao 
elif produto3 == 'arroz':
    total += varroz
elif produto3 == 'macarrao':
    total += vmacarrao
print(f'o valor da sua compra é {total}')
