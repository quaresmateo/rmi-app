from datetime import datetime

import Pyro4

server = Pyro4.Proxy(f"PYRONAME:rmi.server")


class Person:
    def __init__(self, email, name, lastname, picture, address, formation, skills, expirience):
        self.email = email
        self.name = name
        self.lastname = lastname
        self.picture = picture
        self.address = address
        self.formation = formation
        self.skills = skills
        self.expirience = expirience


class Option:
    def __init__(self, text, data):
        self.text = text
        self.data = data


def start_resquest():
    option = Option('', 0)

    while (option != 'exit'):
        print('Escolha a as opções')
        print('[1] Criar usuário')
        print('[2] Ver usuário por curso')
        print('[3] Ver habilidade de pessoas por cidade')
        print('[4] Ver experiência de pessoa')
        print('[5] Ver experiência do usuário')
        print('[6] Ver todos os usuários')
        print('[7] Ver infomações de um usuário')

        option.text = input("... ")

        if(option.text == "1"):
            # Criar usuário
            email = input('Email: ')
            name = input('Nome: ')
            lastname = input('Sobrenome: ')
            picture = input('Foto (link): ')
            address = input('Recidência: ')
            formation = input('Formação acadêmica: ')
            skills = input('Habilidades: ')
            expirience = input('Experiência: ')
            option.data = Person(email, name, lastname, picture,
                                 address, formation, skills, expirience)
        now = datetime.now()
        print(f'Enviado às {now:%H:%M:%S:%f} \n')
        response = server.send_response(option)
        print(response)
        scanf = input()


if __name__ == '__main__':
    try:
        start_resquest()
    except (KeyboardInterrupt, EOFError):
        print('Goodbye! (:')
exit
