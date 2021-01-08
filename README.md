# Files

This project actually contains 2 separate projects in 1 repo.The first project is meant to measure the distance between the
person's face and the camera by using the ultrasonic distance measurement sensor.The name of the files of the first project are
"face_detection.py","ultrasonic.ino" and "face.xml" for detecting face.Here are the components of the first project.

# Components

![](https://github.com/Moeed1mdnzh/Distance-Detection/blob/master/components.jpg)

-A logitech or hayic webcam
-A hc-sr04 ultrasonic sensor
-An arduino board
-Cable
-4 male and female wires

#Circuit

To complete the circuit, connect the first wire to the VCC ping of ultrasonic sensor and the other head to the 5V of arduino,
then connect the second wire to the trig pin and the other head to the 13th pin of arduino,connect the third wire to the echo pin
and the 11th pin and for the last wire which is really simple just connect it to the GND of ultrasonic sensor pin and arduino's GND pin.
After completing the whole circuit you can simply somehow connect the sensor to the webcam, I myself used tape to connect it.Remember 
you need to know the name of your cable port otherwise it won't work.After figuring out your cable's port name replace the "COM4" port name in 
the fourth line of the face_detection.py file with your port name.

# Distance-measurement-without-sensors

SO the second project is for the people who already don't have the components of the previous circuit.
It includes the "dist_and_face.py" file and "face.xml" file for the haar algorithm to detect your face.
The second project works without arduino and it's only pure python code. The way that it measures the distance
between your face and the webcam is that as you get closer to the webcam the size of the rectangle around your face increases
which means that when you are too close to webcam the size of the rectangle is also close to the size of the current frame.
So it basically depeneds on the rectangle's size.
