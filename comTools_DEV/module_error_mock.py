import cybertron
import sys
import time
from protopy import metric_alarm_pb2 as metric

module_id = 0
errcode = 0
msg_in = ""

if len(sys.argv) == 4:
    module_id = int(sys.argv[1])
    errcode = int(sys.argv[2])
    msg_in = str(sys.argv[3])

node = cybertron.node.Node("module_error_test_")
writer = node.create_writer("/monitor/channel_metric_alarm", metric.MetricAlarm)
msg = metric.MetricAlarm()

msg.mode_num = module_id
msg.fault_num = errcode
msg.msg = msg_in 

print(msg)
while cybertron.init.ok():
    time.sleep(0.01)
    writer.write(msg)
