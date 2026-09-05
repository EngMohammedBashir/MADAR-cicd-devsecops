import os

os.environ.setdefault("MADAR_DB_PASSWORD", "dummy-test-only")

from app import app


def test_health_endpoint_returns_ok():
    client = app.test_client()

    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.get_json() == {
        "status": "ok",
        "service": "madar-legacy-app",
    }
