FROM python:3.9-slim

RUN apt-get update \
  && apt-get install -y curl \
  && apt-get clean

RUN pip3 install requests

# Install Ollama
RUN curl https://ollama.com/install.sh | sh

WORKDIR /usr/src/app

CMD ["ollama", "serve" ]
