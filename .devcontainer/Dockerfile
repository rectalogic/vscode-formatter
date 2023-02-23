FROM ubuntu:jammy

RUN apt-get -y update && apt-get install -y git python3 python3-dev python3-venv python3-distutils build-essential
RUN python3 -m venv /site/venv && /site/venv/bin/pip install black
