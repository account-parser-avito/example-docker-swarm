FROM python:3.8.3-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip3 install --upgrade pip
COPY . .

RUN pip3 install -r requirements.txt
EXPOSE 5010


CMD ["python3", "run_service.py"]
