from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Main(Resource):
    def get(self):
        return 'Use /add/a/b to call the API which returns the sum of a and b.'

class Add(Resource):
    def get(self, num1, num2):
        return {'result': num1+num2}

api.add_resource(Main, '/')
api.add_resource(Add, '/add/<int:num1>/<int:num2>')

if __name__ == '__main__':
    app.run(debug=True)