FROM python:3.9-slim-buster

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt &&\
    apt update &&\
    apt install -y curl

COPY app/ app
WORKDIR app/

EXPOSE 8080

HEALTHCHECK --interval=10s CMD curl --fail http://localhost:8080/healthz || exit 1

ENTRYPOINT ["python"]
CMD ["api.py"]
