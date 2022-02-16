FROM python:3.11.0a5-alpine3.15

COPY / /Python-Network-Tools/
WORKDIR /Python-Network-Tools
RUN apk -U upgrade
RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "pnt3.py" ]
