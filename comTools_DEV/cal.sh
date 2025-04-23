#!/bin/bash
cal_file=$1
log_str=$2
if [[ -z $cal_file ]];then
    echo "please input cal_file"
    exit 1
fi
echo $cal_file
start_time=$(cat $cal_file |grep "$(date +'%Y')" |head -n 1|awk '{print $1, $2}')
end_time=$(cat $cal_file |grep "$(date +'%Y')" |tail -n 1|awk '{print $1, $2}')
echo "时间区间:${start_time} —— ${end_time}"
cat $cal_file |awk 'BEGIN{i=0;sum=0}{i+=1;sum+=$3}END{print "内存:采集点数:"i,"平均内存占用："sum/i/1024"MB" }'

cat $cal_file |awk '{print $3}'|sort -n |awk 'BEGIN{i=0}{dict[i]=$1/1024;i+=1}END{
    a_50=int(i*0.5);
    a_80=int(i*0.80);
    a_90=int(i*0.90);
    a_95=int(i*0.95);
    a_99=int(i*0.99);
    a_999=int(i*0.999);
    a_9999=int(i*0.9999);
    a_99999=int(i*0.99999);
    min=1;
    max=i-1
    print "内存占用：50分位:"dict[a_50], "80分位:"dict[a_80], "90分位:"dict[a_90],"95分位:"dict[a_95],"99分位:"dict[a_99], "99.9分位:"dict[a_999], "99.99分位:"dict[a_9999], "99.999分位:"dict[a_99999], "最小:"dict[min], "最大:"dict[max]}'
cat $cal_file |awk 'BEGIN{i=0;sum=0}{i+=1;sum+=$4}END{print "cpu:采集点数:"i,"平均cpu占用："sum/i"%" }'
cat $cal_file |awk '{print $4}'|sort -n |awk 'BEGIN{i=0}{dict[i]=$1;i+=1}END{
    a_50=int(i*0.5);
    a_80=int(i*0.80);
    a_90=int(i*0.90);
    a_95=int(i*0.95);
    a_99=int(i*0.99);
    a_999=int(i*0.999);
    a_9999=int(i*0.9999);
    a_99999=int(i*0.99999);
    min=1;
    max=i-1
    print "cpu占用：50分位:"dict[a_50], "80分位:"dict[a_80], "90分位:"dict[a_90],"95分位:"dict[a_95],"99分位:"dict[a_99], "99.9分位:"dict[a_999], "99.99分位:"dict[a_9999], "99.999分位:"dict[a_99999], "最小:"dict[min], "最大:"dict[max]}'

if [[ -z $log_str ]];then
    echo "please input log_str, cal log"
    exit 1
fi
ls -ll   ~/xlog/nvme/panel_server.* | grep $log_str |awk 'BEGIN{i=0;sum=0}{i+=1;sum+=$5}END{print "日志文件数:"i,"总大小:"sum, "平均每分钟日志大小："sum/60/1024/1024 "MB" }'