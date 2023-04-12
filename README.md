# Canvas-on-the-air - CoreXY pen plotter incorprated with OpenCV gesture recgonition
This project combines a CoreXY pen plotter with OpenCV gesture recognition.\
With this setup, you can draw pictures or write messages simply by making gestures with your hand!

### Getting Started


### CoreXY pen plotter
Computer with OpenCV installed
Webcam or other camera for gesture recognition
Once you have these components, you can follow these steps to set up the project:

### Clone this repository to your local machine.
1. Connect your CoreXY pen plotter to your computer via USB.
2. Install dependencies from the file 
3. Connect your webcam or other camera to your computer.
4. Run the Universal-G-Code-Sender application to connect the computer to arduino using grbl
4. Run the 'backend.py' script to start the backend software, coomunicating gcode signal to arduino.
5. Run the 'app.py' script to start the plotter control software.
6. Make gestures with your hand to control the plotter and draw pictures!

### Project Structure
This project consists of the following files:

**README.md**: This file, which provides an overview of the project.\
**gesture_recognition.py**: Python script that uses OpenCV to recognize gestures and send commands to the plotter.\
**plotter_controller.py**: Python script that communicates with the CoreXY pen plotter and executes commands received from the gesture recognition script.

### References
https://www.instructables.com/How-to-Control-a-Servo-Using-GRBL/ \
https://github.com/winder/Universal-G-Code-Sender \
https://github.com/grbl/grbl

### Contributing
Contributions to this project are welcome! If you find a bug or have an idea for a new feature, please open an issue or submit a pull request.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
