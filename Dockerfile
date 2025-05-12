FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

RUN mkdir /app

WORKDIR /app


COPY requirements.txt pyproject.toml uv.lock /app/

RUN uv pip install --system -r requirements.txt


COPY . /app/

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
