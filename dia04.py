# Simulador de progresso de estudos

meta = 120
horas_estudadas = 0
horas_por_dia = 7

while horas_estudadas < meta:
    horas_estudadas += horas_por_dia
    semana = horas_estudadas // 10
    print(f'Horas estudadas: {horas_estudadas} | Semana aproximada: {semana}")')

    if horas_estudadas == 60:
        print('---Metade da jornada!---')
    if horas_estudadas >= meta:
        print('Meta atingida! Você está pronta para o mercado.')