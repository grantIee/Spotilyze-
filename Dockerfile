FROM alpine 
RUN apk add python3 
RUN apk add --no-cache --virtual .build-deps g++ python3-dev libffi-dev openssl-dev && \
    apk add --no-cache --update python3 && \
    pip3 install --upgrade pip setuptools
RUN pip3 install pendulum service_identity

COPY . . 
RUN python3 -m pip3 install -r src/requirements.txt 
EXPOSE 5000 

CMD python3 src/app.py
