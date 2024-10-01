FROM python:3.9-slim

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install nbconvert

ENV PYTHONUNBUFFERED=1

COPY . .

CMD ["bash"]
