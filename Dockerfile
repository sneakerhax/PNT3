FROM python:3

COPY /network_tools3.py /modules /requirements.txt /scripts /Python-Network-Tools/
WORKDIR /Python-Network-Tools
RUN pip install -r requirements.txt

ENTRYPOINT [ "python", "network_tools3.py" ]
