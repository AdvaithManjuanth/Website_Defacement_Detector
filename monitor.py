import time
import subprocess

while True:
    subprocess.run(["python", "detector.py"])
    time.sleep(300)