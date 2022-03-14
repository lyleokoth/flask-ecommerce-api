import pytest
from ecom import app


@pytest.fixture
def client():
    return app.test_client()


def test_home(client):
    resp = client.get('/api')
    assert resp.status_code == 200
