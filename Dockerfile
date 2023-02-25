FROM python:3.10-slim as python

ENV PYTHONBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    VENV_PATH=/opt/.venv

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential default-libmysqlclient-dev gcc curl

WORKDIR /app

FROM python as poetry
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV PATH="$POETRY_HOME/bin:$PATH"

RUN curl -sSL https://install.python-poetry.org | python3 -
COPY pyproject.toml poetry.lock ./
RUN poetry install --only main --no-interaction --no-ansi -vvv


FROM python as runtime
ENV TZ="Asia/Almaty"
ENV PATH="/app/.venv/bin:$PATH"
COPY --from=poetry /app /app