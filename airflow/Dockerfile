FROM python:3.9-slim-buster

ARG AIRFLOW_VERSION=2.2.3

ENV AIRFLOW_HOME=/usr/local/airflow
ENV PYTHONPATH="${PYTHONPATH}:${AIRFLOW_HOME}"

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    freetds-bin \
    freetds-dev \
    libffi6 \
    libffi-dev \
    libkrb5-dev \
    libsasl2-2 \
    libsasl2-dev \
    libssl1.1 \
    libssl-dev \
    libpq-dev \
    locales \
    lsb-release \
    netcat \
    rsync \
    sasl2-bin \
    wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN locale-gen en_US.UTF-8

RUN pip install --upgrade pip && \
    pip install apache-airflow==$AIRFLOW_VERSION \
    --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

RUN useradd -ms /bin/bash -d ${AIRFLOW_HOME} airflow

COPY scripts/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
COPY config/airflow.cfg ${AIRFLOW_HOME}/airflow.cfg
RUN chown -R airflow: ${AIRFLOW_HOME}

USER airflow
WORKDIR ${AIRFLOW_HOME}

ENTRYPOINT ["/entrypoint.sh"]
CMD ["webserver"]
