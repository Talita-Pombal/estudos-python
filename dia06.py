# "recebe matérias e horas" - parâmetros da função
def resumo_estudos (materia1, materia2, materia3, horas1, horas2, horas3) :
    #"somar todas as horas" - variavel em soma
    total = horas1 + horas2 + horas3
    #"descobrir qual é a maior" - comparação
    if horas1 > horas2 and horas1 > horas3:
        mais_estudadas = materia1
    elif horas2 > horas3:
        mais_estudadas  = materia2
    else:
        mais_estudadas = materia3

    #"mostrar o resultado" - print
    print(f"Total de horas estudadas: {total}") 
    print(f'Materia com mais horas: {mais_estudadas}')     
resumo_estudos ('Python', 'Git', 'Lógica', 10, 3, 5)