docker-machine ssh $1 "nohup ./kafka/bin/zookeeper-server-start.sh \
    kafka-config/zookeeper.properties > kafka/zookeeper.log &"
