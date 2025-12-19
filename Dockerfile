FROM python:3.10-slim

WORKDIR /srv
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

ENTRYPOINT ["python", "-m", "app"]