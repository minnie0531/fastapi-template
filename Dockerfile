FROM python:3.9-slim
  
WORKDIR /app/

COPY . /app/
COPY ./requirements.txt /app/

RUN ./setup.sh
CMD python3 entrypoint.py
