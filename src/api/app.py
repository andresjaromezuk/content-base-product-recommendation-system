
import sys
import os
project_root = os.path.abspath(os.path.join(os.getcwd(), '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

from flask import Flask, Blueprint
from flask_restful import Api

from items import ItemResource

app = Flask(__name__)

api_v1_0_bp = Blueprint('api_v1_0_bp', __name__, url_prefix='/api')

api = Api(api_v1_0_bp)

api.add_resource(ItemResource, 
                 '/items', 
                 '/items/<int:item_id>',
                 '/items/<string:action>')

app.register_blueprint(api_v1_0_bp)

if __name__ == '__main__':
    app.run(debug=True)