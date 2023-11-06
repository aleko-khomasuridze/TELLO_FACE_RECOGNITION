# ----------------------------------------------------------------------------
# Real-Time Face Detection and Drone Control Script
# Author: Aleko Khomasuridze
# Date: 04.12.2022
#
# Description:
# This script integrates real-time face detection and annotation with drone control using the DJI Tello drone. It captures
# video from a specified camera, detects faces in each frame, and adds annotations to the detected faces. Additionally, it
# displays the battery status of the drone. While designed for drone control, the drone control section is currently
# commented out for safety reasons, and users should uncomment and customize it for their specific needs.
#
# Important Note:
# Ensure that the Haar Cascade XML file, "haarcascade_frontalface_default.xml," is present in the specified directory.
#
# Dependencies:
# - OpenCV (cv2)
# - numpy
# - faceDraw (custom module or script)
# - djitellopy (DJI Tello Python wrapper)
# ----------------------------------------------------------------------------

# Import necessary libraries
import time
import cv2
import numpy as np
from faceDraw import faceDraw
from djitellopy import tello

# Initialize variables for drone control
upDownVal = 200
leftRightVal = 300

# Open a video capture object (assumes camera at index 1)
cap = cv2.VideoCapture(1)

# Initialize a Tello drone object and perform initial setup
me = tello.Tello()
me.connect()
me.streamon()
me.takeoff()
time.sleep(0.1)

# Adjust drone control values for various movements
me.send_rc_control(0, 0, 50, 0)
time.sleep(0.5)
me.send_rc_control(0, 0, 0, 0)

# Create a new Tello drone object (this is redundant)
me = tello.Tello()

# Define min and max values for up/down and left/right movements
UDmin = 70
LRmin = 90
LRmax = 345
UDmax = 315

me.streamon()

# Print the path to the OpenCV library file
print(cv2.__file__)

# Define design and basic colors
frame_f     = (240, 85, 60)   # Bright green
frame_b     = (248, 181, 50)  # Darker green
label_color = (90, 72, 240)   # Purple

blue    = (0xFF, 0x00, 0x00)
green   = (0x00, 0xFF, 0x00)
red     = (0x00, 0x00, 0xFF)
purple  = (0xFF, 0x00, 0xFF)
yellow  = (0x00, 0xFF, 0xFF)
cyan    = (0xFF, 0xFF, 0x00)
white   = (0xFF, 0xFF, 0xFF)

# Function to convert a value from one range to another
def convert(num, minVal, maxVal, conMinVal, conMaxVal):
    pass

# Function to find and annotate faces in an image
def findFace(img):
    # Load the Haar Cascade classifier for face detection
    faceCascade = cv2.CascadeClassifier("C:\\Users\\aleko\\OneDrive\\Desktop\\tello_face_recog\\cascades\\data\\haarcascade_frontalface_default.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 8)

    myFaceListC = []
    myFaceListArea = []

    for (x, y, w, h) in faces:
        # Draw an outline around the detected face
        faceDraw.frame(img, x, y, w, h, label_color, 20, 2)

        # Draw a crosshair on the center of the face
        faceDraw.center(img, x, y, w, h, frame_f, "crossHair", 15)

        # Draw a label to display the person's name (in this case, "unknown")
        faceDraw.label(img, x, y, w, h, frame_f, "unknown".upper(), white)

        upDownVal = y + h // 2
        leftRightVal = x + w // 2

        # Get the dimensions of the video frame
        width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) // 2
        height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) // 2

        line_color = yellow

        # Draw a line connecting the center of the face with the center of the frame
        cv2.line(img, (x + w // 2, y + h // 2), (width, height), line_color, 2)

        # Drone control logic (currently commented out)
        '''
        if upDownVal <= ((UDmax-UDmin)//2)-20 and upDownVal >= UDmin:
            me.send_rc_control(0, 0, 50, 0)
            print("Tello moving -> UP")
        elif upDownVal >= ((UDmax-UDmin)//2)+20 and upDownVal <= UDmax:
            me.send_rc_control(0, 0, -50, 0)
            print("Tello moving -> DOWN")
        elif leftRightVal >= ((LRmax-LRmin)//2)-20 and leftRightVal <= LRmax:
            me.send_rc_control(0, 0, 0, -50)
            print("Tello moving -> RIGHT")
        elif leftRightVal <= ((LRmax-LRmin)//2)+20 and leftRightVal >= LRmin:
            me.send_rc_control(0, 0, 0, 50)
            print("Tello moving -> LEFT")
        else:
            me.send_rc_control(0, 0, 0, 0)
            print("Waiting for a face...")
            line_color = green
        '''

# Main loop for video processing
while True:
    width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) // 2
    height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) // 2
    bat = 100  # Battery level (currently hardcoded, replace with actual battery data)
    _, img = cap.read()
    findFace(img)

    # Determine the color for displaying battery status
    color = None
    if bat <= 20:
        color = (106, 95, 245)  # Low battery color
    else:
        color = (245, 185, 71)  # Normal battery color

    # Display battery status on the frame
    cv2.putText(img, "BATTERY AT {}%".format(bat), (6, 30), cv2.FONT_HERSHEY_DUPLEX, 1, color, 2)

    # Draw a white rectangle in the center of the frame
    cv2.rectangle(img, (width - 20, height - 20), (width + 20, height + 20), white, 2)

    # Display the frame in a window named "frame"
    cv2.imshow("frame", img)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        #me.land()  # Currently commented out for safety
        break

# Release the video capture object and close the OpenCV window when done
cap.release()
cv2.destroyAllWindows()
