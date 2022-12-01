FROM python:3.10-slim-bullseye as production

ENV PYTHONPATH "${PYTHONPATH}:/app"
ENV PATH "/app/scripts:${PATH}"

EXPOSE 5000
WORKDIR /app

# Install Poetry
RUN set +x \
 && apt update \
 && apt upgrade -y \
 && apt install -y curl gcc build-essential \
 && curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python -\
 && cd /usr/local/bin \
 && ln -s /opt/poetry/bin/poetry \
 && poetry config virtualenvs.create false \
 && rm -rf /var/lib/apt/lists/*

# Add code & install dependencies
COPY pyproject.toml poetry.lock /app/
RUN poetry install -n --only main --no-root

ADD . /app/
RUN chmod +x scripts/* \
 && poetry install -n --only-root

ENTRYPOINT ["docker-entrypoint.sh"]
