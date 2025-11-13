FROM python:3.13-slim

ENV PYTHONDOWNWRITEBYCODE=1 \
    PYTHONUMBAFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends build-essential libffi-dev && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt 

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app/

ENV FLASK_APP=wsgi.py \ 
    FLASK_ENV=development

EXPOSE 5001

CMD ["flask", "run", "--host=0.0.0.0","--port=5001"]