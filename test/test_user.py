from typing import Any

import pytest
from httpx import AsyncClient
from test.dummy_data import test_user_1, test_user_2


class TestTelegramUserEndpoints:

    @staticmethod
    async def create_or_get_user(client: AsyncClient) -> dict[str, Any]:
        response = await client.post(
            url='/api/users/telegram_user/',
            json=test_user_2,
        )
        return response.json()

    @staticmethod
    async def create_or_get_driver(user_id: int, client: AsyncClient) -> dict[str, Any]:
        response = await client.post(
            url='/api/users/telegram_driver/',
            json={'user_id': user_id},
        )
        return response.json()

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
        user_data = await self.create_or_get_user(client)
        created_driver = await client.post(
            url="/api/users/telegram_driver/",
            json={'user_id': user_data['detail']['id']}
        )
        driver_data = created_driver.json()
        assert driver_data['status'] == 'success'
        assert driver_data['detail']['user_id'] == user_data['detail']['id']

    @pytest.mark.asyncio
    async def test_telegram_trip(self, client: AsyncClient) -> None:
        user_data = await self.create_or_get_user(client)
        driver_data = await self.create_or_get_driver(user_data['detail']['id'], client)
        created_trip = await client.post(
            url="/api/trips/telegram_create_trip/",
            json={
                "driver_id": driver_data['detail']['id'],
                "car_model": "X",
                "car_number": "11",
                "number_of_seats": 1,
                "origin": "A",
                "start_lat": 0,
                "start_lon": 0,
                "destination": "B",
                "end_lat": 0,
                "end_lon": 0,
                "start_time": "2025-05-07T16:04:13.664Z",
                "end_time": "2025-05-07T16:04:13.664Z"
            }
        )

        trip_data = created_trip.json()

        assert trip_data['status'] == 201
        assert trip_data['detail']['driver_id'] == driver_data['detail']['id']


class TestHealthCheck:

    @pytest.mark.asyncio
    async def test_dummy(self, client: AsyncClient) -> None:
        res = await client.get("/")
        assert res.status_code in [200, 404]
