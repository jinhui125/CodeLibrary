#!/bin/bash
#set -x
set -e
pid=$1
echo -e "time\tmem\tcpu"
while true
do
	mem=`cat /proc/${pid}/status |grep VmRSS|awk '{print $2}'`
	cpu=`top -b  -p ${pid} -d 1 -n 1 |grep ${pid}|awk '{print $9}'`
	echo -n `date +'%Y-%m-%d %H:%M:%S'`
	echo -e "\t${mem}\t${cpu}"
	sleep 2
done