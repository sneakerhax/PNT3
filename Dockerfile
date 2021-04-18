FROM python:3

COPY / /Python-Network-Tools
WORKDIR /Python-Network-Tools
RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "network_tools3.py" ]
