FROM python:3.7.4-buster as PII_project

ENV PYTHONDONTWRITEBYTECODE=1
ARG PIIHOME=/home/$USER/PII_project
WORKDIR $PIIHOME

RUN apt-get update \
&& apt-get -y install build-essential libpoppler-cpp-dev pkg-config python3-dev \
&& mkdir -p output \
&& rm -rf /var/lib/apt/lists/* \
&& useradd --create-home --shell /bin/bash $USER \
&& chown -R $USER:$USER $PIIHOME


COPY requirements.txt ./
COPY PII_removal.py ./
COPY main.py ./

RUN pip3 install -r requirements.txt

COPY input/ input/

VOLUME ["/home/$USER/PII_project/output"]
ENTRYPOINT ["python3", "/home/$USER/PII_project/main.py"]
