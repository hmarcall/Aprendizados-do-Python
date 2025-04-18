dicio = {
    'Henrique': [8,9],
    'João': [9,8],
    'Maria': [9,4],
    'Mainá': [7,1],
    'Pedro': [8,6]
}
for chave, valor in dicio.items():
    media = sum(valor) / len(valor)
    print(chave,media)