FROM python:3.7.6-alpine3.10

RUN mkdir -p /app

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN apk --update add --virtual build-dependencies python-dev py-pip build-base \
  && pip install --upgrade pip \
  && pip install -r requirements.txt \
  && apk del build-dependencies

COPY ./ ./

CMD uvicorn main:app --host 0.0.0.0