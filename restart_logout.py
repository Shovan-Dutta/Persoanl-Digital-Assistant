import subprocess

#for restarting or logging out the computer the computer
def restart():
    subprocess.call(["shutdown", "/r", "/t", "60"])
    return
def logout():
    subprocess.call(["shutdown", "/l ", "/t", "60"])
    return