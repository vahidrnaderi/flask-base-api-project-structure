# import app
from app.app import apiv1
from .resource import Resource

# GET /api/v1/resources/?query={query}
# POST /api/v1/resources/
apiv1.add_resource(
    Resource,
    "/resources/",
    methods=["GET", "POST"],
    endpoint="resources",
)

# GET /api/v1/resources/{id}
# PUT /api/v1/resources/{id}
# DELETE /api/v1/resources/{id}
apiv1.add_resource(
    Resource,
    "/resources/<resource_id>",
    methods=["GET", "PUT", "PATCH", "DELETE"],
    endpoint="resource",
)
