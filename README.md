# 🏭 Predictive Maintenance MLOps System

Система предиктивной аналитики для прогнозирования износа и аварийных поломок оборудования на основе телеметрии датчиков.

---

## 📁 Структура репозитория

```text
project_name/
│
├── README.md              # Документация проекта
├── requirements.txt       # Зависимости Python
├── .gitignore             # Игнорируемые файлы для Git
├── .env.example           # Шаблон переменных окружения
│
├── data/                  # Данные (не отслеживаются Git, кроме примеров)
│   ├── raw/               # Сырые данные с датчиков
│   ├── processed/         # Очищенные датасеты
│   └── samples/           # Небольшие примеры для тестов
│
├── sql/                   # SQL-скрипты и витрины данных
│   ├── schema.sql         # Схема базы данных
│   ├── layers.sql         # Слои трансформации (Bronze/Silver/Gold)
│   └── queries.sql        # Аналитические запросы
│
├── notebooks/             # Jupyter-ноутбуки исследований
│   ├── 01_data_preparation.ipynb
│   ├── 02_baseline_model.ipynb
│   ├── 03_model_experiments.ipynb
│   └── 04_final_model.ipynb
│
├── src/                   # Исходный код пайплайна
│   ├── data/              # Скрипты загрузки и фичи (features.py)
│   ├── models/            # Обучение и инференс моделей
│   ├── utils/             # Вспомогательные утилиты
│   └── etl_pipeline.py    # ETL-процессы
│
├── api/                   # REST API на базе FastAPI
│   └── main.py
├── streaming/             # Скрипты потоковой обработки (Kafka / Redis)
├── tests/                 # Автотесты (Unit и Integration)
├── deployment/            # Конфигурации Docker и Kubernetes
│
└── docs/                  # Документация и схемы архитектуры
