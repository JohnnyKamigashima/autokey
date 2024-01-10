import subprocess

keyboard.send_keys("<ctrl>+c")

def window_exists(window_name):
    try:
        subprocess.check_output(["wmctrl", "-l"])
        return True
    except subprocess.CalledProcessError:
        return False

if window_exists("Obsidian"):
    subprocess.call(["wmctrl", "-a", "Obsidian"])
else:
    subprocess.call(["obsidian"])

keyboard.send_keys("<enter>")    
keyboard.send_keys("<ctrl>+v")