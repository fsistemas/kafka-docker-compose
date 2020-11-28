# Repo to create Kafka cluster - single node

## What is inside
- Zookeeper
- Kafka single node
- Tool to create topics based on desired state file kafka-git-opts
- kafka-rest proxy to use kafka-topics-ui
- kafka-topics-ui to see topics and messages
- kafka python producer
- kafka python consumer

# Start environment:
docker-compose down --remove-orphans && docker-compose up --remove-orphans --build
