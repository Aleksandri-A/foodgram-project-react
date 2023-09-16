FROM python:3.9

WORKDIR /app

COPY requirements.txt .

COPY run.sh .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

RUN chmod +x run.sh

ENTRYPOINT ["/app/run.sh"]
