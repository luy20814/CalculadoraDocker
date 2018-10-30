import sumTwoNumbers
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class sumNumbers(Resource):
    def get(self, first_number):
        return {'resultado': sumTwoNumbers.sumTwo(first_number)}

class resNumbers(Resource):
    def get(self, first_number, second_number):
     return {'resultado': sumTwoNumbers.resTwo(first_number,second_number)}
	 
class mulNumbers(Resource):
    def get(self, first_number):
     return {'resultado': sumTwoNumbers.mulTwo(first_number)}
	 
class divNumbers(Resource):
    def get(self, first_number, second_number):
     return {'resultado': sumTwoNumbers.divTwo(first_number,second_number)}

api.add_resource(sumNumbers, '/sumnumbers/<first_number>')
api.add_resource(resNumbers, '/restwonumbers/<first_number>:<second_number>')
api.add_resource(mulNumbers, '/mulnumbers/<first_number>')
api.add_resource(divNumbers, '/divtwonumbers/<first_number>:<second_number>')

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=80)