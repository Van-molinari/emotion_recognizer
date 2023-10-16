FROM python:3.10.8

WORKDIR /usr/backend

COPY requirements.txt ./

RUN apt update

RUN apt-get -y install portaudio19-dev

RUN pip install --upgrade pip 

RUN pip install -r requirements.txt

RUN apt-get -y update && apt-get -y upgrade && apt-get install -y --no-install-recommends ffmpeg

COPY . .

EXPOSE 5500

CMD [ "python", "run.py", "--", "--host" ]