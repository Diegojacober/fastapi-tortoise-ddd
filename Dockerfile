FROM python:slim
LABEL maintainer="diegojacober"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./ /app
WORKDIR /app
EXPOSE 8000


RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client jpeg-dev && \
    apk add --update --no-cache --virtual .tmp-build-deps \
    build-base postgresql-dev musl-dev zlib zlib-dev linux-headers && \
    /py/bin/pip install setuptools && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    rm -rf /tmp && \
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home \
    fastapi-user && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    chown -R fastapi-user:fastapi-user /vol && \
    chmod -R 777 /vol

ENV PATH="/py/bin:$PATH"

USER fastapi-user