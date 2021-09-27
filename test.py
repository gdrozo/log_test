import subprocess
import sys
import re
import time

wait_hours = 12  #Stop for 12 hours and then run again
run_hours = 3/60    #We will run ngrep for an hour. The nth run will be dumped to net_log_n.txt
run_time_limit = 100    #Suppose you only want to take a log for 100 hours while you are away.

ngrep_cmd = "sudo ngrep -w byline port 80> net_log_.txt"
subprocess.call([ngrep_cmd], shell=True)
time.sleep(run_hours*3600)
subprocess.call(["sudo killall ngrep"], shell=True)