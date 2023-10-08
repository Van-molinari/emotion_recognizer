FROM python:3.10.8

WORKDIR /usr/backend

COPY requirements.txt ./

RUN pip install --upgrade pip 

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5500

CMD [ "python", "run.py", "--", "--host" ]