# Apache Kafka

## Install

### MacOS

```bash
brew install kafka
```

Tested on M3 Macbook Pro, the base directory of kafka is `/opt/homebrew/opt/kafka/bin`.

## Basic Usage

```
# Version 확인
./bin/kafka-topics.sh --version

# Zookeeper 실행
./bin/zookeeper-server-start.sh ./config/zookeeper.properties

# Kafka 실행
./bin/kafka-server-start.sh ./config/server.properties

# Topic 생성
./bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --topic stock-update

# Topic 생성 - partitions, replication-factor
./bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --topic stock-update --partitions 1 --replication-factor 1

# Topic 확인
./bin/kafka-topics.sh --describe --bootstrap-server localhost:9092 --topic stock-update

# Topic 목록
./bin/kafka-topics.sh --list --bootstrap-server localhost:9092

# Topic 삭제
./bin/kafka-topics.sh --delete --bootstrap-server localhost:9092 --topic stock-update

# Producer
./bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic stock-update

# Producer - Key, Value
./bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic stock-update --property "parse.key=true" --property "key.separator=:" --property "print.key=ture"

# Producer - Message
ABCDE

# Producer - Key, Value Message
key:{"val1":"A","val2":"B","val3":3}

# Consumer
./bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic stock-update --from-beginning

# Consumer Group 확인
./bin/kafka-consumer-groups.sh --list --bootstrap-server localhost:9092

# Consumer Group Topic 확인
./bin/kafka-consumer-groups.sh --describe --bootstrap-server localhost:9092 --group stock-update-group
```
