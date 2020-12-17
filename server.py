from datetime import datetime

import Pyro4


@Pyro4.expose
class Bot(object):
    def send_response(self, option, person):
        now = datetime.now()
        print(f'{option} {person} - Recebido às {now:%H:%M:%S:%f} \n')

        return 0


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
