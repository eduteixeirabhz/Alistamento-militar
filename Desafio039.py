from datetime import date
atual = date.today().year
nasc = int(input('Qual é o ano de seu nascimento? '))
idade = atual - nasc
print('Quem nasceu em {}, tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você deve se alistar no Exército')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda falta(m) {} ano(s) para o seu alistamento '.format(saldo))
elif idade - 18:
    saldo = idade - 18
    print(' Você já deveria ter se alistado há {} ano(s)'.format(saldo))
