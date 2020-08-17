# import subprocess
# import sys
# import os
# import re
# ping = subprocess.Popen('ping -c 2 192.168.50.1',
#                             shell=True,
#                             stderr=subprocess.PIPE,
#                             stdout=subprocess.PIPE)  # 执行命令
#
# ret = str(ping.communicate())
# print(ret)
# loss_re = re.compile(r'received, (.*) packet loss')
# packet_loss = loss_re.findall(ret)[0]
# print(packet_loss)
#
#
#
# rtt_re = re.compile(r"min/avg/max/stddev = (.*) ")
# rtts = rtt_re.findall(ret)
#
# print(rtts)
#
#
# # rtt.split(["/"])
# rtt = rtts[0].split('/')
# print(rtt)
# rtt_min = rtt[0]
# rtt_avg = rtt[1]
# rtt_max = rtt[2]
# print("%s\t\t%s\t\t%s\t\t%s\t\t%s" % ('192.168.50.1', packet_loss, rtt_min, rtt_max, rtt_avg))