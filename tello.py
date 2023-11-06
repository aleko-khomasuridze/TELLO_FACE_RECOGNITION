# ----------------------------------------------------------------------------
# Real-Time Face Detection and Annotation Script
# Author: Aleko Khomasuridze
# Date: 04.12.2022
#
# Description:
# This script utilizes the OpenCV library to perform real-time face detection and annotation. It captures video from
# the default camera and detects faces in each frame. Detected faces are embellished with annotations such as
# outlines, crosshairs, and labels. Additionally, a green rectangle is positioned in the center of the video frame to
# highlight it. The script continuously processes frames from the camera until the 'q' key is pressed to exit the loop.
#
# Important Note:
# Ensure that you have the required Haar Cascade XML file, "haarcascade_frontalface_default.xml," in the specified
# directory ("cascades\\data") for accurate face detection.
# ----------------------------------------------------------------------------


# Import necessary libraries
import cv2
from faceDraw import faceDraw  # Assuming there's a custom "faceDraw" module or script

# Open the default camera (camera index 0)
cap = cv2.VideoCapture(0)

# Define colors for various elements
frame_f     = (240, 85,  60)    # Bright green
frame_b     = (248, 181, 50)    # Darker green
label_color = (90, 72,  240)    # Purple

# Define basic colors in BGR format
blue    = (0xFF, 0x00, 0x00)
green   = (0x00, 0xFF, 0x00)
red     = (0x00, 0x00, 0xFF)
purple  = (0xFF, 0x00, 0xFF)
yellow  = (0x00, 0xFF, 0xFF)
cyan    = (0xFF, 0xFF, 0x00)
white   = (0xFF, 0xFF, 0xFF)

# Function to detect faces in an image and annotate them
def findFace(img):
    # Load the Haar Cascade classifier for face detection
    faceCascade = cv2.CascadeClassifier("cascades\\data\\haarcascade_frontalface_default.xml")

    # Convert the image to grayscale
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = faceCascade.detectMultiScale(imgGray, scaleFactor=1.2, minNeighbors=8)

    # Iterate through detected faces and annotate them
    for (x, y, w, h) in faces:
        # Draw an outline around the detected face
        faceDraw.frame(img, x, y, w, h, label_color, 20, 2)

        # Draw a crosshair on the center of the face
        faceDraw.center(img, x, y, w, h, frame_f, "crossHair", 15)

        # Draw a label to display the person's name (in this case, "unknown")
        faceDraw.label(img, x, y, w, h, frame_f, "unknown".upper(), white)

        # Get the dimensions of the video frame
        width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) // 2
        height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) // 2

        # Define the color for the line that connects face center with frame center
        line_color = yellow

        # Draw a line connecting the center of the face with the center of the frame
        cv2.line(img, (x + w // 2, y + h // 2), (width, height), line_color, 2)

# Continuously capture and process frames from the camera
while True:
    middle_box_height = 30  # Height of the middle box

    # Get the dimensions of the video frame
    width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) // 2
    height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) // 2

    # Read a frame from the camera
    _, img = cap.read()

    # Detect and annotate faces in the frame
    findFace(img)

    # Draw a green rectangle in the center of the frame
    cv2.rectangle(img, (width - middle_box_height // 2, height - middle_box_height // 2),
                  (width + middle_box_height // 2, height + middle_box_height // 2), green, 2)

    # Display the frame in a window named "frame"
    cv2.imshow("frame", img)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows when done
cap.release()
cv2.destroyAllWindows()
