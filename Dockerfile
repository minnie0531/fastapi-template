FROM rhel8/python-39
  
WORKDIR /app/

COPY . /app/
COPY ./requirements.txt /app/

RUN ./setup.sh
CMD python3 entrypoint.py
