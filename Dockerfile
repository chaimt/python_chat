FROM python:3
VOLUME /tmp

CMD export app_folder = reporting
RUN mkdir -p /opt/tikal/chat/log
RUN mkdir -p /opt/tikal/chat/data

ENV DOCKER_BASEDIR /opt/docker
ENV DOCKER_LOGDIR  ${DOCKER_BASEDIR}/log
ENV DOCKER_SCRIPTS_DIR  ${DOCKER_BASEDIR}/scripts

RUN pip3 install virtualenv
RUN virtualenv --no-download env -p python3.6
# Set virtualenv environment variables. This is equivalent to running
# source /env/bin/activate
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt && pip install -U six
RUN mkdir app
COPY ./app ./app/

CMD bash -x ${DOCKER_SCRIPTS_DIR}/startup.sh reporting | tee -a ${DOCKER_LOGDIR}/startup.log

