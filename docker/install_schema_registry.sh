docker-machine ssh $1 "wget -qO - http://packages.confluent.io/deb/3.0/archive.key | sudo apt-key add -"
docker-machine ssh $1 'sudo add-apt-repository "deb [arch=amd64] http://packages.confluent.io/deb/3.0 stable main"'
docker-machine ssh $1 "sudo apt-get update && sudo apt-get install openjdk-8-jre && sudo apt-get install openjdk-8-jdk"
docker-machine ssh $1 "sudo apt-get install confluent-platform-2.11"
docker-machine ssh $1 \
    'echo "
listeners=http://0.0.0.0:8081
kafkastore.connection.url=$2:2181
kafkastore.topic=_schemas
debug=false" > schema-registry.properties'
