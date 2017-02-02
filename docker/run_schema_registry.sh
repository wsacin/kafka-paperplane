docker-machine ssh $1 "nohup schema-registry-start \
    schema-registry.properties > schema-registry.log &"
