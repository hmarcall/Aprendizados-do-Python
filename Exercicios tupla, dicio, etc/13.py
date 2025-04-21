dicio = {
    'Janeiro': '31',
    'Fevereiro': '28',
    'Março': '31',
    'Abril': '30',
    'Maio': '31',
    'Junho': '30',
    'Julho': '31',
    'Agosto': '31',
    'Setembro': '30',
    'Outubro': '31',
    'Novembro': '30',
    'Dezembro': '31'
}
digite= str(input('Digite um mês(ex: Setembro): ')).capitalize()
if digite in dicio:
    print('O mês de', digite, 'tem', dicio[digite], 'dias.')
else:
    print('Mês inválido.')
