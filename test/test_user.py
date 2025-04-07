import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest.mark.asyncio
async def test_telegram_login():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.post("/api/users/telegram_login/", json={
            "telegram_id": -1,
            "username": "test_user2",
            "phone_number": "+996555000112",
            "auth_method": "telegram"
        })

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert data["detail"]["telegram_id"] == -1
