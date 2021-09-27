from os import error
import subprocess
import time
import threading

wait_hours = 12  #Stop for 12 hours and then run again
run_hours = 1/60    #We will run ngrep for an hour. The nth run will be dumped to net_log_n.txt
run_time_limit = 100    #Suppose you only want to take a log for 100 hours while you are away.

def capture():
    ngrep_cmd = "sudo ngrep -W byline port 80"
    print('running process')
    try:
        result = subprocess.check_output([ngrep_cmd], shell=True, stderr=subprocess.STDOUT, timeout=run_hours*3600)
        print(result)
    except error as e:
        print(e.output)

t = threading.Thread(target=capture)
t.start()
print('Sleeping')
time.sleep(run_hours*3600)
print('Killing the process')
#subprocess.call("sudo killall ngrep", shell=True)
print('done')
