FROM python:3.10-slim-bookworm

WORKDIR /app

RUN apt-get update && apt-get install --no-install-recommends -y \
    curl && \
    curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

COPY ./pyproject.toml ./poetry.lock* /app/

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --only main ; fi"

RUN useradd -m chatter

COPY ./Chatter/ /app/Chatter/
COPY ./static/ /app/static/
COPY ./token.json /app/token.json

RUN chown -R chatter:chatter /app

USER chatter

CMD ["uvicorn", "Chatter.App.App:app", "--host", "0.0.0.0", "--port", "5002"]
