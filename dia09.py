# Lista de comensais
comensais = ["Amanda", "Patricia", "Tarso", "Sabrina", "Camila", "Sara"]
print(comensais)
print(comensais[0])
print(comensais[-1])
print(len(comensais))
for comensal in comensais:
    print(f"Comensal: {comensal}")
    comensais.append('Pablo')
print(f'Comensais atualizado: {comensais}')
comensais.remove('Patricia')
print(f'Após remoção: {comensais}')