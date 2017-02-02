docker-machine ssh $1 "nohup ./kafka/bin/kafka-server-start.sh kafka-config/server$2.properties > kafka/kafka$2.log &"
