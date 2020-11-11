# FROM python:3.7-slim
FROM registry.access.redhat.com/ubi8/ubi

USER 0
RUN yum install -y python3; yum clean all
# ENV PYTHONUNBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN python3 -m pip install -r requirements.txt
RUN chown -R 1001:0 /app && chmod -R 774 /app

USER 1001

ENTRYPOINT ["python3"]
CMD ["/app/app.py"]
