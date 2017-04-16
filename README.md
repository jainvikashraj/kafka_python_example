

Setup:
	> pip install kafka

Setup Kafka Binaries:
	wget "http://www-eu.apache.org/dist/kafka/0.9.0.0/kafka_2.11-0.9.0.0.tgz"
	tar xvzf kafka_2.11-0.9.0.0.tgz

Create Topic:
	bin/kafka-topics.sh --create --zookeeper 10.140.216.18:2181 --replication-factor 1 --partitions 1 --topic test

Producer Code:
	kproduder.py

Consumer Code:
	kconsumer.py

Reference:
	http://kafka-python.readthedocs.io/en/master/usage.html
	http://techblog.netflix.com/2016/04/kafka-inside-keystone-pipeline.html

Author:
	Vikash Jain
