# O programa diz o que o usuário estudar com base nos dias da semana que estão armazenados em uma lista

#definir uma função com um parametro
#criar uma lista com os dias da semana
#arranjar alguma forma de pegar aleatoriamente uma semana da lista e jogar como parâmetro na hora de jogar na tela

import random


def oqueFazer(resposta):
    if resposta == 'Segunda':
        return 'Estudar HTML'
    elif resposta == 'Terça':
        return 'Estudar CSS'
    elif resposta == 'Quarta':
        return 'Estudar JavaScript'
    elif resposta == 'Quinta':
        return 'Revisar HTML e CSS'
    elif resposta == 'Sexta':
        return 'Fazer um projeto utilizando HTML, CSS e JS'
    elif resposta == 'Sábado':
        return 'Have a beer'
    elif resposta == 'Doming':
        return 'Vá ao cinema ou fique em casa lendo um livro'

diasDaSemana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
print(oqueFazer(random.choice(diasDaSemana)))


