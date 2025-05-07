import pytest
from httpx import AsyncClient
from test.dummy_data import test_user_1, test_user_2


class TestTelegramUserEndpoints:

    @pytest.mark.asyncio
    async def test_telegram_login(self, client: AsyncClient) -> None:
        response = await client.post(
            url="/api/users/telegram_user/",
            json=test_user_1,
        )

        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert data["detail"]["telegram_id"] == -1
        assert data["detail"]["username"] == "@test_user1"

    @pytest.mark.asyncio
    async def test_telegram_driver(self, client: AsyncClient) -> None:
        created_user = await client.post(
            url="/api/users/telegram_user/",
            json=test_user_2,
        )
        user_data = created_user.json()
        assert user_data['detail']['telegram_id'] == -2

        created_driver = await client.post(
            url="/api/users/telegram_driver/",
            json={'user_id': user_data['detail']['id']}
        )
        driver_data = created_driver.json()
        assert driver_data['status'] == 'success'
        assert driver_data['detail']['user_id'] == user_data['detail']['id']


class TestHealthCheck:

    @pytest.mark.asyncio
    async def test_dummy(self, client: AsyncClient) -> None:
        res = await client.get("/")
        assert res.status_code in [200, 404]

