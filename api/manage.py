from app.main import create_app
from app.main.service.data_service import prepare_data
from app import blueprint

app = create_app()
app.register_blueprint(blueprint)

app.app_context().push()

def run():
    app.run(debug=True, port=4000)

# def prepare_data():


if __name__ == '__main__':
    prepare_data()
    run()