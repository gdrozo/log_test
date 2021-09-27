import subprocess
import sys
import re
import time

keep_running = 1 #Loop flag
wait_hours = 12  #Stop for 12 hours and then run again
run_hours = 1    #We will run ngrep for an hour. The nth run will be dumped to net_log_n.txt
f_num=0
hours_so_far=0
run_time_limit = 100    #Suppose you only want to take a log for 100 hours while you are away.
while keep_running:
    ngrep_cmd = "sudo ngrep -ixW >  net_log_" + str(fnum) + ".txt &"
    subprocess.call([ngrep_cmd], shell=True)
    time.sleep(run_hours*3600)
    subprocess.call(["sudo killall ngrep"], shell=True)
    time.sleep(wait_hours*3600)
    f_num += 1
    hours_so_far += run_hours
    if hours_so_far >= run_time_limit:
        keep_running = 0