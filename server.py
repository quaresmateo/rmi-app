# from pony.orm import *
# from pony.orm.serialization import to_dict
# import json
from datetime import datetime
from pony import orm
import Pyro4

db = orm.Database()

db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
orm.set_sql_debug(True)


class Person(db.Entity):
    email = orm.Required(str, unique=True)
    name = orm.Required(str)
    lastname = orm.Required(str)
    picture = orm.Required(str)
    address = orm.Required(str)
    formation = orm.Required(str)
    skills = orm.Required(str)
    expirience = orm.Required(str)


db.generate_mapping(create_tables=True)


@Pyro4.expose
class Bot(object):
    def send_response(self, option, data):
        now = datetime.now()
        print(f'{option} - Recebido às {now:%H:%M:%S:%f} \n')

        if option == '1':
            with orm.db_session:
                # Criar pessoa no banco de dados
                person = Person(
                    email=data['email'],
                    name=data['name'],
                    lastname=data['lastname'],
                    picture=data['picture'],
                    address=data['address'],
                    formation=data['formation'],
                    skills=data['skills'],
                    expirience=data['expirience']
                )
                orm.commit()
            data = 'Usuário criado com sucesso!'

        elif option == '2':
            with orm.db_session:
                persons = orm.select(
                    person for person in Person if person.formation == data)[:]
                q = {'data': [p.to_dict() for p in persons]}
                data = q
                print('Mostrando usuário por curso')

        elif option == '3':
            with orm.db_session:
                persons = orm.select(
                    person.skills for person in Person if person.address == data)[:]
                q = {'data': [p for p in persons]}
                data = q
                print('Solicitação de habilidades por cidade')

        elif option == '4':
            with orm.db_session:
                persons = orm.select(
                    person for person in Person if person.email == data['email'])[:]
                q = {'data': [p.to_dict() for p in persons]}
                person = q['data'][0]
                id = person['id']
                Person[id].expirience += f', {data["expirience"]}'
                print('Experiênia adicionada!')

        elif option == '5':
            with orm.db_session:
                persons = orm.select(
                    person for person in Person if person.email == data)[:]
                q = {'data': [p.to_dict() for p in persons]}
                person = q['data'][0]
                name = person['name']
                lastname = person['lastname']
                expirience = person['expirience']
                data = {'name': name + ' ' + lastname,
                        'expirience': expirience}
                print('Mostrando experiência por pessoa')

        elif option == '6':
            with orm.db_session:
                persons = orm.select(person for person in Person)[:]
                data = {'data': [p.to_dict() for p in persons]}
                print('Mostrando todas as pessoas')

        elif option == '7':
            with orm.db_session:
                persons = orm.select(
                    person for person in Person if person.email == data)[:]
                q = {'data': [p.to_dict() for p in persons]}
                data = q['data'][0]
                print('Mostrando informações de uma pessoa')

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
