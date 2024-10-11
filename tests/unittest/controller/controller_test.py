import pytest

API = "/api/v1/resources"

# PUT /api/v1/resources/{id}
@pytest.mark.parametrize(
    ("headers", "data", "resource_id", "status"),
    [
        ({}, {}, "test", 415),  # Missing Content-Type, invalid request
        ({"Content-Type": "application/json"}, {}, "test", 400),  # Missing data in JSON
        ({"Content-Type": "application/json"}, {"value": "new resource"}, "invalid_id", 404),  # Invalid resource ID
        ({"Content-Type": "application/json"}, {"value": "updated resource", "category": "new_category"}, "existing_id", 200),  # Valid update
    ]
)
def test_update_resource(client, headers, data, resource_id, status):
    print(f"-{headers=}--{data=}--{resource_id=}--{status=}----")
    response = client.put(
        f"{API}/{resource_id}",
        json=data,
        headers=headers
    )
    assert response.status_code == status

# GET /api/v1/resources/{id}
@pytest.mark.parametrize(
    ("headers", "resource_id", "status"),
    [
        ({""}, "test", 415),  # Missing Content-Type
        ({"Content-Type": "application/json"}, "nonexistent_id", 404),  # Resource not found
        ({"Content-Type": "application/json"}, "existing_id", 200),  # Resource found
    ]
)
def test_get_resource(client, headers, resource_id, status):
    response = client.get(
        f"/api/v1/resources/{resource_id}",
        headers=headers
    )
    assert response.status_code == status

# POST /api/v1/resources/
@pytest.mark.parametrize(
    ("headers", "data", "status"),
    [
        ({""}, {""}, 415),  # Missing Content-Type
        ({"Content-Type": "application/json"}, {""}, 404),  # Missing value in body
        ({"Content-Type": "application/json"}, {"value": "test resource"}, 201),  # Valid resource creation
        ({"Content-Type": "application/json"}, {"value": "duplicate resource", "category": "test"}, 409),  # Duplicate resource (if validation is implemented)
    ]
)
def test_create_resource(client, headers, data, status):
    response = client.post(
        "/api/v1/resources/",
        json=data,
        headers=headers
    )
    assert response.status_code == status

# DELETE /api/v1/resources/{id}
@pytest.mark.parametrize(
    ("headers", "resource_id", "status"),
    [
        ({""}, "test", 415),  # Missing Content-Type
        ({"Content-Type": "application/json"}, "nonexistent_id", 404),  # Resource not found
        ({"Content-Type": "application/json"}, "existing_id", 200),  # Resource successfully deleted
    ]
)
def test_delete_resource(client, headers, resource_id, status):
    response = client.delete(
        f"/api/v1/resources/{resource_id}",
        headers=headers
    )
    assert response.status_code == status

# GET /api/v1/resources/?query={query}
@pytest.mark.parametrize(
    ("headers", "query", "status"),
    [
        ({""}, "test", 415),  # Missing Content-Type
        ({"Content-Type": "application/json"}, "", 404),  # No query given
        ({"Content-Type": "application/json"}, "resource_search", 200),  # Valid search query
    ]
)
def test_search_resources(client, headers, query, status):
    response = client.get(
        f"/api/v1/resources/?query={query}",
        headers=headers
    )
    assert response.status_code == status
