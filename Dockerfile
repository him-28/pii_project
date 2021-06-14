FROM python:3.7.4-buster as pii_project

ENV PYTHONDONTWRITEBYTECODE=1
ARG PIIHOME=/home/himanshu/pii_project
WORKDIR $PIIHOME

RUN apt-get update \
&& apt-get -y install build-essential libpoppler-cpp-dev pkg-config python3-dev \
&& mkdir -p output \
&& rm -rf /var/lib/apt/lists/* \
&& useradd --create-home --shell /bin/bash himanshu \
&& chown -R himanshu:himanshu $PIIHOME


COPY requirements.txt ./
COPY PII_removal.py ./
COPY main.py ./

RUN pip3 install -r requirements.txt

COPY input/ input/

VOLUME ["/home/himanshu/pii_project/output"]
ENTRYPOINT ["python3", "/home/himanshu/pii_project/main.py"]
