FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir \
    --index-url https://download.pytorch.org/whl/cpu \
    torch \
    torchvision \
    torchaudio && \
    pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

CMD ["python3", "./src/app.py"]