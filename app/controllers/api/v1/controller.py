from flask import current_app, request
from app.util import jsonify


class Controller:

    # PUT /api/v1/resources/{id}
    # Endpoint to update a resource by unique id. If the resource does not exist,
    # return 404 not found. But if it does, store a updated version locally.
    # Any subsequent reads should only see this updated version.
    def update_resource(self, resource_id):
        current_app.logger.debug(f"controllers ===> PUT /api/v1/resources/{resource_id}")
        current_app.logger.debug(f"body = {request.get_json()=}")

        return jsonify(status=501)

    # GET /api/v1/resources/{id}
    # Endpoint to retrieve a resource by unique id.
    # You should take local and remote results into consideration.
    def get_resource(self, resource_id):
        current_app.logger.debug(f"controllers ===> GET /api/v1/resources/{resource_id}")

        return jsonify(status=501)

    # POST /api/v1/resources/
    # Endpoint to create resource locally.
    def create_resource(self):
        current_app.logger.debug("controllers ===> POST /api/v1/resources/")
        current_app.logger.debug(f"body = {request.get_json()=}")

        return jsonify(status=501)

    # DELETE /api/v1/resources/{id}
    # Endpoint to delete a resource by unique id. If the resource does not exist,
    # return 404 not found. But if it does, mark the resource locally as deleted.
    # Any subsequent reads should NOT see this resource.
    def delete_resource(self, resource_id):
        current_app.logger.debug(f"controllers ===> DELETE /api/v1/resources/{resource_id}")

        return jsonify(status=501)

    # GET /api/v1/resources/?query={query}
    # Free text search endpoint. You should take local and
    # remote search results into consideration.
    def search_resources(self, query):
        current_app.logger.debug(f"controllers ===> GET /api/v1/resources/?query={query}")

        return jsonify(status=501)
