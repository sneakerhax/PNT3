FROM python:alpine

COPY / /Python-Network-Tools/
WORKDIR /Python-Network-Tools
RUN apk -U upgrade
RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "pnt3.py" ]
