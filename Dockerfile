FROM python:3
RUN pip install flask
RUN pip install requests
ENTRYPOINT ["python", "src/server.py"]