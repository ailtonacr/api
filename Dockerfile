FROM python:3.12 as base

WORKDIR /api

COPY requirements.txt .

RUN pip install -r requirements.txt --root-user-action=ignore

COPY /src .

FROM base AS local

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "--reload", "api:app"]
