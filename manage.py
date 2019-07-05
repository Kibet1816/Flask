from app import create_app,db

app = create_app('development')
# app = create_app('production')
# app = create_app('tests')

if __name__ == '__main__':
    app.run()