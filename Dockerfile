FROM ubuntu:22.04

# تثبيت المتطلبات الأساسية
RUN apt-get update && \
    apt-get install -y git build-essential cmake python3 python3-pip && \
    pip3 install --no-cache-dir -r requirements.txt

WORKDIR /app
COPY . /app

# بناء llama.cpp
RUN git clone https://github.com/ggerganov/llama.cpp
RUN cd llama.cpp && make

EXPOSE 8000

CMD ["python3", "server_api.py"]
