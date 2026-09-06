import os
from unittest.mock import MagicMock, patch

os.environ.setdefault("MADAR_DB_PASSWORD", "dummy-test-only")

from app import app


def test_health_endpoint_returns_ok_without_database_check():
    client = app.test_client()

    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.get_json() == {
        "status": "ok",
        "service": "madar-legacy-app",
    }


def test_ready_returns_503_when_database_is_unavailable():
    client = app.test_client()

    with patch("app.get_db_connection", side_effect=Exception("synthetic DB failure")):
        response = client.get("/api/ready")

    assert response.status_code == 503
    assert response.get_json() == {
        "status": "error",
        "service": "madar-legacy-app",
        "database": "unavailable",
    }


def test_ready_returns_200_when_database_query_succeeds():
    client = app.test_client()
    cursor = MagicMock()
    cursor.__enter__.return_value = cursor
    cursor.__exit__.return_value = False
    connection = MagicMock()
    connection.cursor.return_value = cursor

    with patch("app.get_db_connection", return_value=connection):
        response = client.get("/api/ready")

    assert response.status_code == 200
    assert response.get_json() == {
        "status": "ok",
        "service": "madar-legacy-app",
        "database": "connected",
    }
    cursor.execute.assert_called_once_with("SELECT 1;")
    connection.close.assert_called_once_with()
