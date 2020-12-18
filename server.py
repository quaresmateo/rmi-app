from datetime import datetime

import Pyro4


@Pyro4.expose
class Bot(object):
    def send_response(self, option, data):
        now = datetime.now()
        print(f'{option} - Recebido às {now:%H:%M:%S:%f} \n')
        if option == '1':
            pass
        elif option == '2':
            pass
        elif option == '3':
            pass
        elif option == '4':
            pass
        elif option == '5':
            pass
        elif option == '6':
            pass
        elif option == '7':
            pass
        else:
            data = 'Opção inválida'

        return (data, f'Recebido às {now:%H:%M:%S:%f} \n')


def start_server():
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    uri = daemon.register(Bot)
    ns.register('rmi.server', str(uri))
    print(f'Rodando...')
    daemon.requestLoop()


if __name__ == '__main__':
    try:
        start_server()
    except (KeyboardInterrupt, EOFError):
        print('Goodbye! (:')
exit
