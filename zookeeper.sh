#!/bin/bash
nums=$1
i=1
pssh -h ip -l root -i "sed -i '2c JAVA_HOME=/usr/local/jdk1.8.0_351' /root/zookeeper/bin/zkEnv.sh"
for IP in `cat ip`
do
  if ((i<=nums));then
    pssh -H root@${IP} -l root -i "echo ${i} > /root/zookeeper/dataDir/myid; sed -i '11d' /root/zookeeper/conf/zoo.cfg"
    pssh -H root@${IP} -l root -i "sed -i '11c dataDir=/root/zookeeper/dataDir' /root/zookeeper/conf/zoo.cfg"
    pssh -h ip -l root -i "echo server.${i}=${IP}:2888:3888 >> /root/zookeeper/conf/zoo.cfg"
    i=$((i+1))
  fi
done

pssh -h ip -l root -i "cat /root/zookeeper/dataDir/myid"
pssh -h ip -l root -i "cat /root/zookeeper/conf/zoo.cfg |grep dataDir"
pssh -h ip -l root -i "cat /root/zookeeper/conf/zoo.cfg |grep server"
pssh -h ip -l root -i "bash /root/zookeeper/bin/zkServer.sh start"

