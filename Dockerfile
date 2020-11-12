FROM registry.access.redhat.com/ubi8/ubi

USER 0
RUN yum install -y python3; yum clean all

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./
RUN chown -R 1001:0 /app && \
  chmod -R 774 /app && \
  mkdir /.cache && chown -R 1001:0 /.cache && \
  mkdir /.local && chown -R 1001:0 /.local

USER 1001
RUN python3 -m pip install -r requirements.txt --user

ENTRYPOINT ["python3"]
CMD ["/app/app.py"]
