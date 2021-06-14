FROM python:3.7.4-buster as PII_project

ENV PYTHONDONTWRITEBYTECODE=1
ARG HOME=~/PII_removal
WORKDIR $HOME

RUN apt-get update \
&& apt-get -y install build-essential libpoppler-cpp-dev pkg-config python3-dev \
&& mkdir -p output \
&& rm -rf /var/lib/apt/lists/* \
&& useradd --create-home --shell /bin/bash $USER \
&& chown -R $USER:$USER $HOME


COPY requirements.txt ./
COPY PII_removal.py ./
COPY main.py ./

RUN pip3 install -r requirements.txt

COPY input/ input/

VOLUME ["~/PII_removal/output"]
ENTRYPOINT ["python3", "~/PII_removal/main.py"]
