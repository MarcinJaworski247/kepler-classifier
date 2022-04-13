from flask_restx import Api
from flask import Blueprint

from .main.controller.data_controller import api as data_ns
from .main.controller.stats_controller import api as stats_ns
from .main.controller.plots_controller import api as plots_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Exoplanet classification Flask REST API',
          version='1.0',
          )

api.add_namespace(data_ns, path='/data')
api.add_namespace(stats_ns, path='/stats')
api.add_namespace(plots_ns, path='/plots')