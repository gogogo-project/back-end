from random import randint


dummy_client = {
    "telegram_id": str(randint(1_000_000, 1_000_000_009)),
    "name": "John Doe",
    "phone_number": "+9876543210"
}

dummy_user = {
    "id": 0,
    "telegram_id": str(randint(1_000_000, 1_000_000_009)),
    "name": "John Doe",
    "phone_number": "+9876543210",
    "is_blocked": False,
    "blocked_at": None,
}
