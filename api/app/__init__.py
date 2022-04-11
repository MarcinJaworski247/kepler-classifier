from flask_restx import Api
from flask import Blueprint

from .main.controller.data_controller import api as data_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(data_ns, path='/data')