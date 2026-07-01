# Lista básicas
cardapio = ["arroz", "feijão", "frango", "salada", "suco", "sobremesa"]

print(cardapio)
print(cardapio[0])
print(cardapio[-1])
print(len(cardapio))

for prato in cardapio:
    print(f'Prato disponivel: {prato}')

cardapio.append('fruta')
print(f'Cardápio atualizado: {cardapio}')

cardapio.remove('suco')
print(f'Após remoção: {cardapio}')