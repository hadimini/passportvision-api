FROM python:3.12-slim

WORKDIR /backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

RUN apt-get update \
    && apt-get -y install --no-install-recommends \
    gcc \
    postgresql \
    && apt-get clean

RUN useradd -m -u 1000 backenduser && chown -R backenduser:backenduser /backend

USER backenduser

RUN pip install --upgrade pip
COPY --chown=backenduser:backenduser ./requirements.txt /backend/requirements.txt
RUN pip install --user --no-cache-dir -r requirements.txt

COPY --chown=backenduser:backenduser . /backend
