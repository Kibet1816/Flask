from app import create_app,db
from flask_script import Manager,Server,Shell


app = create_app('development')
# app = create_app('production')
# app = create_app('tests')

manager = Manager(app)

manager.add_command('server',Server)


if __name__ == '__main__':
    manager.run()