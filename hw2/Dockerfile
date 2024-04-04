FROM redis

RUN apt-get -y update && apt-get install -y nano
RUN apt install -y python3 && apt-get install -y pip

COPY ./main.py /main.py
COPY ./requirements.txt /requirements.txt
COPY ./json_file.json /json_file.json

RUN pip install -r /requirements.txt --break-system-packages
