from datetime import datetime

import Pyro4

server = Pyro4.Proxy(f"PYRONAME:rmi.server")


def start_resquest():
    option = ''
    data = ''

    while (option != 'exit'):
        print('Escolha a as opções')
        print('[1] Criar usuário')
        print('[2] Ver usuário por curso')
        print('[3] Ver habilidade de pessoas por cidade')
        print('[4] Adicionar experiência à pessoa')
        print('[5] Ver experiência de uma pessoa')
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
            data = {
                'email': email,
                'name': name,
                'lastname': lastname,
                'picture': picture,
                'address': address,
                'formation': formation,
                'skills': skills,
                'expirience': expirience
            }
        elif option == '2':
            course = input('Informe o nome do curso: ').strip()
            data = course
        elif option == '3':
            city = input('Informe o nome da cidade: ').strip()
            data = city
        elif option == '4':
            email = input('Informe o email: ').strip()
            expirience = input('Adicionar experiência: ').strip()
            data = {
                'email': email,
                'expirience': expirience
            }
        elif option == '5':
            email = input('Informe o email: ').strip()
            data = email
        elif option == '6':
            pass
        elif option == '7':
            email = input('Informe o email: ').strip()
            data = email
        else:
            data = 'Opção inválida'

        now = datetime.now()
        print(f'Enviado às {now:%H:%M:%S:%f} \n')
        (response, date) = server.send_response(option, data)
        print(response)
        print(date)
        scanf = input('\n `Enter` para continuar...')


if __name__ == '__main__':
    try:
        start_resquest()
    except (KeyboardInterrupt, EOFError):
        print('Goodbye! (:')
exit
