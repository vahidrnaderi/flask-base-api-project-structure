#           Copyright 2024 vahidrnaderi@gmail.com

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from json import load as json_load
from flask import Flask, Blueprint, jsonify
from flask_restful import Api

from .config import Config

apiv1_bp = Blueprint(
    name="apiv1_bp",
    import_name=__name__,
    url_prefix="/api/v1",
)

apiv1 = Api(apiv1_bp)

from . import resources

# Aplication factory structure
def create_app(config_file=None):
    app = Flask(__name__)
    app.config.from_object(Config)
    if config_file is not None:
        app.config.from_file(config_file, load=json_load)

    # Register APIv1 blueprint to application.
    app.register_blueprint(apiv1_bp)

    @app.route('/api/v1/routes', methods=['GET'])
    def list_routes():
        output = []
        for rule in app.url_map.iter_rules():
            methods = ','.join(rule.methods)
            output.append({
                "endpoint": rule.endpoint,
                "rule": rule.rule,
                "methods": methods
            })

        return jsonify(output)

    return app
