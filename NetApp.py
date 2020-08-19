from appJar import gui
import os
import time
# py file that I created which contains an array
# called ipaddr which contains ip addresses
from iplist import *

#get the int value of length of array
y = len(ipaddr)

#set GUI object 
app = gui("Welcome Primus", "400x200")
app.setBg("grey")
app.setFont("20")

#runs through array to display value
#app.addLabel("ipaddress", ipaddr)
for y in range(0, y):
    app.addLabel(y, ipaddr[y], colspan=2)

#test to see if its connected, if not, return background red
def netping(*args):
    y = len(ipaddr)
    alert = "red"
    okay = "grey"
    for x in range(0, y):
        response = os.system("ping -n 3 -w 500 " + ipaddr[x])
        if response == 0:
            app.setLabelBg(x, okay)
        else:
            app.setLabelBg(x, alert)

#close app function
def closebtn():
    app.stop()
    sys.exit()
#var to set the buttons at the bottom of the row
z = y + 1

#set the app buttons
app.addButton("ping", netping, z, 0)
app.addButton("close", closebtn, z, 1)

#loop the ping func every 30 sec
def looping():
    while True:
        netping()
        time.sleep(30)

#see the process in runtime
print(os.getpid())

#thread the loop
app.thread(looping)

#start the app
app.go()





