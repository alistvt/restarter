import os
import signal
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def find_pids(filename):
    process = "python {}".format(filename)
    stream = os.popen("ps -eaf | grep {}".format(filename))
    output = stream.read()
    pids = []
    for line in output.splitlines():
        if process in line:
            pids.append(int(line.split()[1]))
    return pids


def kill_process(pids):
    for pid in pids:
        try:
            logging.info(f"killing process {pid}")
            stream = os.kill(pid, signal.SIGKILL)
            logging.info("process got killed.")    
        except ProcessLookupError as e:
            logging.info("process is already killed.")


if __name__ == '__main__':
    filename = "program-to-be-restarted.py"
    pids = find_pids(filename)
    kill_process(pids)
