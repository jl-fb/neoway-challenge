FROM python:3-alpine

# Add Maintainer Info
LABEL maintainer="Joao Borghezan <jlborgh@gmail.com>"

WORKDIR /src

COPY requirements.txt ./
RUN apk add --update --no-cache g++ gcc libxslt-dev libxml2
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


CMD [ "python", "main.py" ]