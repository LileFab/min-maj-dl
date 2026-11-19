FROM python:3.13-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

COPY . .


FROM python:3.13-slim

RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY --from=builder /install /usr/local
COPY --from=builder /app /app

WORKDIR /app/minmaj_music_dl

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate --noinput && exec gunicorn minmaj_music_dl.wsgi:application --bind 0.0.0.0:8000"]
