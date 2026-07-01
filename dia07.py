# "calcular o custo da refeição por comensal em uma UAN"
def custo_total(alimentar, descartaveis, limpeza, despesas_indiretas, mao_de_obra, custo_fixo, imposto, lucro):
    total = alimentar + descartaveis + limpeza + despesas_indiretas + mao_de_obra + custo_fixo + imposto + lucro

#”mostrar o resultado” - print

    print(f"Custo da refeição por comensal: R$ {total}")

custo_total(14, 3, 2, 5, 4, 5, 3, 3)