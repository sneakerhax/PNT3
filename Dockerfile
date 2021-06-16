FROM python:3.8.8-slim-buster

COPY / /Python-Network-Tools/
WORKDIR /Python-Network-Tools
RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "network_tools3.py" ]
