import json

'''3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;'''

with open("dados.json") as arquivo:
    dados = json.load(arquivo)
    menor = {}
    maior = {}
    dia = 0
    media = 0
    for c in range(len(dados)):
        if c == 0:
            maior = dados[c]
            menor = dados[c]
        else:
            if dados[c]["valor"] > maior["valor"]:
                maior = dados[c]
            if dados[c]["valor"] < menor["valor"]:
                menor = dados[c]
        if dados[c]["valor"] != 0:
            dia += 1
            media += dados[c]["valor"]
    media = media / dia
    dia = 0
    for c in range(len(dados)):
        if dados[c]["valor"] > media:
            dia += 1
    print(f"O menor valor de faturamento foi R${menor['valor']:.2f} e o maior foi R$ {maior['valor']:.2f}.\nTiveram {dia} dias no mês em que o faturamento foi maior que a média mensal de R$ {media:.2f}")