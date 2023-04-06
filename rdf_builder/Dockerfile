FROM python:3.8

RUN apt-get update && apt-get upgrade && apt-get -y install netcat && apt-get clean

RUN python -m pip install --upgrade pip

WORKDIR /code

COPY  requirements.txt .

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code

COPY ./rdf_builder/config.yml ./

COPY run.sh ./

RUN chmod +x ./run.sh

RUN chmod -R 777 ./

CMD ["./run.sh"]