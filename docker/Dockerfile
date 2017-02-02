FROM java:openjdk-8-jre

ENV KAFKA_HOME /app/kafka_2.11-0.10.1.1
ENV LISTENERS PLAINTEXT://0.0.0.0:9092

################# REMOTE SERVER IP ####################
ENV ADVERTISED_LISTENERS PLAINTEXT://my.remote.server.ip:9092

WORKDIR /app

RUN apt-get update && apt-get install -y zookeeper wget
RUN wget http://www-us.apache.org/dist/kafka/0.10.1.1/kafka_2.11-0.10.1.1.tgz
RUN tar xvf kafka_2.11-0.10.1.1.tgz
RUN rm kafka_2.11-0.10.1.1.tgz

ADD config/server.properties "$KAFKA_HOME"/config/

RUN echo listeners=$LISTENERS \
    >> "$KAFKA_HOME"/config/server.properties
RUN echo advertised.listeners=$ADVERTISED_LISTENERS \
    >> "$KAFKA_HOME"/config/server.properties

WORKDIR "$KAFKA_HOME"
