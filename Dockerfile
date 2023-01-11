FROM python:3
RUN pip install flask
RUN pip install requests
RUN mkdir app
COPY src/server.py app/server.py
ENTRYPOINT ["python", "app/server.py"]