# ---- Predictive Maintenance ML API ----
# Базовый образ: slim-сборка Python без лишних системных пакетов
FROM python:3.11-slim

# Не писать .pyc, не буферизовать stdout (логи сразу видны в docker logs),
# корень проекта в PYTHONPATH — иначе не резолвится импорт src.features
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

WORKDIR /app

# curl нужен только для HEALTHCHECK; сразу чистим списки apt, чтобы не раздувать слой
RUN apt-get update \
 && apt-get install -y --no-install-recommends curl \
 && rm -rf /var/lib/apt/lists/*

# Зависимости копируются отдельным слоем: пересборка кода не тянет за собой pip install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Код приложения и артефакт модели
COPY src/ ./src/
COPY api/ ./api/
COPY model.pkl .

# Непривилегированный пользователь — контейнер не должен работать от root
RUN useradd --create-home --shell /bin/bash appuser \
 && chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

# Docker сам следит за живостью сервиса через уже реализованный эндпоинт /health
HEALTHCHECK --interval=30s --timeout=3s --start-period=15s --retries=3 \
    CMD curl -fsS http://localhost:8000/health || exit 1

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
