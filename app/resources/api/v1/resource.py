from flask_restful import Resource
from flask import request, current_app
from app.controllers.api.v1 import Controller
from app.util import jsonify


class Resource(Resource):

    # PUT api/v1/resources/{id}
    def put(self, resource_id=None):
        """
        PUT api/v1/resources --> Not allowed.
        PUT api/v1/resources/ --> Not allowed.
        PUT api/v1/resources/<resource_id> --> Update resource.
        """
        current_app.logger.debug(f"resources ===>  PUT api/v1/resources/{resource_id}")

        return Controller().update_resource(resource_id)

    # GET api/v1/resources/?query={query}
    # GET api/v1/resources/{id}
    def get(self, resource_id=None):
        """
        GET api/v1/resources/?query={query} --> Search query.
        GET api/v1/resources/ --> 404 Not Found.
        GET api/v1/resources --> 404 Not Found.
        GET api/v1/resources/<resource_id> --> resource info.
        """
        current_app.logger.debug("resources ===>  GET api/v1/resources/...")

        query = request.args.get("query", None)

        if query:
            current_app.logger.debug(f"resources ===>  GET api/v1/resources/?query={query}")
            return Controller().search_resources(query)
        elif resource_id:
            current_app.logger.debug(f"resources ===>  GET api/v1/resources/{resource_id}")
            return Controller().get_resource(resource_id)
        else:
            return jsonify(status=404)

    # POST api/v1/resources/
    def post(self):
        """
        POST api/v1/resources/ --> Create new resource.
        POST api/v1/resources --> Create new resource.
        POST api/v1/resources/<resource_id> --> Not allowed.
        """
        current_app.logger.debug("resources ===>  POST api/v1/resources/")

        return Controller().create_resource()

    # DELETE api/v1/resources/{id}
    def delete(self, resource_id=None):
        """
        DELETE api/v1/resources --> Not allowed.
        DELETE api/v1/resources/ --> Not allowed.
        DELETE api/v1/resources/<resource_id> --> Delete resource.
        """
        current_app.logger.debug(f"resources ===>  DELETE api/v1/resources/{resource_id}")

        return Controller().delete_resource(resource_id)
