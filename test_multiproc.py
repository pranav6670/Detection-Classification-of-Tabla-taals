import subprocess
# subprocess.call("cd /home/pranav/Desktop/myfinalProject./test_threading.sh")
bashCommand = "python3 guiGO.py & python3 liveSpectogram.py &"
output = subprocess.check_output(['bash', '-c', bashCommand])
