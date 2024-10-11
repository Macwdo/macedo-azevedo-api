from ninja.testing import TestClient
from api.lawyers.routes import lawyer_router


def test_get_lawyers():
    client = TestClient(lawyer_router)

    client.get("/")
