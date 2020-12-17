from datetime import datetime
from Person import Person
from Option import Option

import Pyro4

server = Pyro4.Proxy(f"PYRONAME:rmi.server")


def start_resquest():
    option = ''

    while (option != 'exit'):
        print('Escolha a as opções')
        print('[1] Criar usuário')
        print('[2] Ver usuário por curso')
        print('[3] Ver habilidade de pessoas por cidade')
        print('[4] Ver experiência de pessoa')
        print('[5] Ver experiência do usuário')
        print('[6] Ver todos os usuários')
        print('[7] Ver infomações de um usuário')

        option = input("... ")

        if(option == "1"):
            # Criar usuário
            email = input('Email: ')
            name = input('Nome: ')
            lastname = input('Sobrenome: ')
            picture = input('Foto (link): ')
            address = input('Recidência: ')
            formation = input('Formação acadêmica: ')
            skills = input('Habilidades: ')
            expirience = input('Experiência: ')
            person = {
                'email': email,
                'name': name,
                'lastname': lastname,
                'picture': picture,
                'address': address,
                'formation': formation,
                'skills': skills,
                'expirience': expirience
            }
        now = datetime.now()
        print(f'Enviado às {now:%H:%M:%S:%f} \n')
        response = server.send_response(option, person)
        print(response)
        scanf = input()


if __name__ == '__main__':
    try:
        start_resquest()
    except (KeyboardInterrupt, EOFError):
        print('Goodbye! (:')
exit
