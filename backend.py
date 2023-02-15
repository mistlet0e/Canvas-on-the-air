#this is the backend file that feeds the coordinates from opencv to arduino with gcode transformation
from flask import Flask
import serial
import time
import ast
from sklearn import preprocessing

app = Flask(__name__)
# Open grbl serial port
s = serial.Serial('/dev/tty.usbmodem2101',115200)

# Wake up grbl
s.write("\r\n\r\n".encode())
time.sleep(2)   # Wait for grbl to initialize 
s.flushInput()  # Flush startup text in serial input

@app.route('/move/<xy_coor>')
def move(xy_coor):
    # show the post with the given id, the id is an integer
    xy_coor = ast.literal_eval(xy_coor)
    gcode = "$J=G21G90" + "X" + str(round((xy_coor[1]/1200)*3.005,3)) + "Y" + str(round((xy_coor[0]/1900)*5.300,3)) + "F300"+ "\n"
    s.write(gcode.encode()) # Send g-code block to grbl
    return f'Moved to {gcode}'


@app.route('/stop')
def stop():
    # show the post with the given id, the id is an integer
    gcode = "M3 S100"+ "\n"
    s.write(gcode.encode())
    return 'now stopped'

@app.route('/down')
def down():
    # show the post with the given id, the id is an integer
    gcode = "M5"+ "\n"
    s.write(gcode.encode())
    return 'now down'








