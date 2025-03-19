FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1
# Установка необходимых инструментов для сборки
RUN apt-get update && apt-get install -y gcc build-essential && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN mkdir /app/database

# Установка Poetry
RUN pip install --upgrade pip "poetry==1.8.4"
RUN poetry config virtualenvs.create false --local
# Копирование файлов конфигурации Poetry
COPY pyproject.toml poetry.lock ./

# Установка зависимостей с помощью Poetry
RUN poetry install --no-dev --no-root

# Копирование проекта
COPY portfolio /app/

# Определение порта
EXPOSE 8000

# Запуск приложения
CMD ["gunicorn", "portfolio.wsgi:application", "--bind", "0.0.0.0:8000"]




