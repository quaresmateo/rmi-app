from datetime import datetime

import Pyro4

server = Pyro4.Proxy(f"PYRONAME:rmi.server")


def start_resquest():
    text = ''
    while (text != 'exit'):
        print('Escolha a as opções')
        print('[1] Criar usuário')
        print('[2] Ver usuário por curso')
        print('[3] Ver habilidade de pessoas por cidade')
        print('[4] Ver experiência de pessoa')
        print('[5] Ver experiência do usuário')
        print('[6] Ver todos os usuários')
        print('[7] Ver infomações de um usuário')
        text = input("... ")
        now = datetime.now()
        print(f'Enviado às {now:%H:%M:%S} \n')
        response = server.send_response(text)
        print(f'Recibido em {response}')
        scan = input()


if __name__ == '__main__':
    try:
        start_resquest()
    except (KeyboardInterrupt, EOFError):
        print('Goodbye! (:')
exit
