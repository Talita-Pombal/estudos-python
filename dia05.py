def calcular_progresso (nome, horas_estudadas):
    meta = 120
    horas_faltantes = meta - horas_estudadas
    dias_faltantes = horas_faltantes / 2

    print(f'Olá, {nome}!')
    print(f'Você estudou {horas_estudadas} horas.')
    print(f'Faltam {horas_faltantes} horas para sua meta.')
    print(f'Com 2h por dia, você termina em {dias_faltantes} dias.')

calcular_progresso('Talita',20)
