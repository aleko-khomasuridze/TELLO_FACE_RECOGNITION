# ----------------------------------------------------------------------------
# faceDraw: OpenCV Annotation Utility
# Author: Aleko Khomasuridze
# Date: 04.12.2022
#
# Description:
# The "faceDraw" class in this code provides a set of utility functions for drawing annotations on images using OpenCV (cv2).
# These annotations include circular frames, frames with labels, center points (crosshairs or circles), and text labels.
# The class can be utilized to enhance visualizations, such as face detection results, in image and video processing applications.
# Ensure that OpenCV is installed to use this utility.
#
# Class Functions:
# - circleFrame(image, X, Y, W, H, radius, color, stroke): Draws circular frames around specified regions.
# - frame(image, X, Y, W, H, color, size, thickness): Draws rectangular frames around specified regions.
# - center(image, X, Y, W, H, color, Type, size): Adds center points (crosshairs or circles) to specified regions.
# - label(image, X, Y, W, H, color, text, text_color): Adds labeled text below specified regions.
# - putTxt(image, X, Y, W, H, color, text): Adds information labels (e.g., X, Y, W, H) next to regions.
#
# Usage:
# To use the "faceDraw" class, instantiate it and call its functions with appropriate parameters.
#
# Example:
# draw = faceDraw()
# draw.frame(image, 10, 10, 100, 100, (0, 255, 0), 10, 2)  # Draws a green frame
# draw.center(image, 50, 50, 100, 100, (0, 0, 255), "crossHair", 10)  # Adds a red crosshair
# draw.label(image, 10, 10, 100, 100, (255, 0, 0), "Sample", (255, 255, 255))  # Adds a labeled text
#
# ----------------------------------------------------------------------------


# Import the OpenCV library with an alias "cv" for image processing
import cv2 as cv

# Create a class "faceDraw" to provide utility functions for image annotation
class faceDraw:
    def __init__(self):
        self.center_point
        self.shade
        self.bgshow

    # Function to draw circular frames around specified regions
    @classmethod
    def circleFrame(cls, image, X, Y, W, H, radius, color, stroke):
        cls.image = image
        cls.X = X
        cls.Y = Y
        cls.W = W
        cls.H = H
        cls.radius = radius
        cls.color = color
        cls.stroke = stroke

        # Draw circles at the specified locations
        cv.circle(image, (X, Y), radius, color, stroke)
        cv.circle(image, (X + W, Y), radius, color, stroke)
        cv.circle(image, (X, Y + H), radius, color, stroke)
        cv.circle(image, (X + W, Y + H), radius, color, stroke)

    # Function to draw rectangular frames around specified regions
    @classmethod
    def frame(cls, image, X, Y, W, H, color, size, thickness):
        cls.image = image
        cls.X = X
        cls.Y = Y
        cls.W = W
        cls.H = H
        cls.color = color
        cls.size = size
        cls.thikness = thickness

        # Draw rectangles to form frames around specified regions
        cv.line(image, (X, Y), (X + size, Y), color, thickness)
        cv.line(image, (X, Y), (X, Y + size), color, thickness)

        cv.line(image, (X + W, Y), (X + W - size, Y), color, thickness)
        cv.line(image, (X + W, Y), (X + W, Y + size), color, thickness)

        cv.line(image, (X, Y + H), (X + size, Y + H), color, thickness)
        cv.line(image, (X, Y + H), (X, Y + H - size), color, thickness)

        cv.line(image, (X + W, Y + H), (X + W - size, Y + H), color, thickness)
        cv.line(image, (X + W, Y + H), (X + W, Y + H - size), color, thickness)

    # Function to add center points (crosshairs or circles) to specified regions
    @classmethod
    def center(cls, image, X, Y, W, H, color, Type, size):
        cls.image = image
        cls.X = X
        cls.Y = Y
        cls.W = W
        cls.H = H
        cls.color = color
        cls.Type = Type
        cls.size = size

        # Calculate the center point of the region
        center_point = (X + W // 2, Y + H // 2)

        if Type == "circle":
            # Draw a circle at the center point
            cv.circle(image, center_point, 5, color, 2)
        elif Type == "crossHair":
            # Calculate coordinates for crosshair lines
            hor_x_pt1 = X + W // 2 - size  # X-coordinate of the horizontal line start point
            hor_y_pt1 = Y + H // 2  # Y-coordinate of the horizontal line start point
            hor_x_pt2 = X + W // 2 + size  # X-coordinate of the horizontal line end point
            hor_y_pt2 = Y + H // 2  # Y-coordinate of the horizontal line end point

            ver_x_pt1 = X + W // 2  # X-coordinate of the vertical line start point
            ver_y_pt1 = Y + H // 2 - size  # Y-coordinate of the vertical line start point
            ver_x_pt2 = X + W // 2  # X-coordinate of the vertical line end point
            ver_y_pt2 = Y + H // 2 + size  # Y-coordinate of the vertical line end point

            # Draw the horizontal and vertical lines to create a crosshair
            cv.line(image, (hor_x_pt1, hor_y_pt1), (hor_x_pt2, hor_y_pt2), color, 2)
            cv.line(image, (ver_x_pt1, ver_y_pt1), (ver_x_pt2, ver_y_pt2), color, 2)

    # Function to add labeled text below specified regions
    @classmethod
    def label(cls, image, X, Y, W, H, color, text, text_color):
        cls.image = image
        cls.X = X
        cls.Y = Y
        cls.W = W
        cls.H = H
        cls.color = color
        cls.text = text
        cls.text_color = text_color

        bgshow = 3
        shade = 30

        # Draw a background rectangle and text label below the region
        cv.rectangle(image, (X + bgshow, Y + H + 8 + bgshow), (X + bgshow + len(text) * 12, Y + H + bgshow + 30),
                     (color[0] - shade, color[1] - shade, color[2] - shade), cv.FILLED)
        cv.rectangle(image, (X, Y + H + 8), (X + len(text) * 12, Y + H + 30), color, cv.FILLED)
        cv.putText(image, text.upper(), (X + 3, Y + H + 24), cv.FONT_HERSHEY_PLAIN, 1, text_color, 2)

    # Function to add information labels (e.g., X, Y, W, H) next to regions
    @classmethod
    def putTxt(cls, image, X, Y, W, H, color, text):
        cls.image = image
        cls.X = X
        cls.Y = Y
        cls.W = W
        cls.H = H
        cls.color = color
        cls.text = text

        lab = ['X', 'Y', 'W', 'H']
        lab_start = 10

        if text == False:
            # Display labels for X, Y, W, H and their respective values
            cv.putText(image, "{}: {}px".format(lab[0], X), (X + W + lab_start, Y + 10), cv.FONT_HERSHEY_PLAIN, 1, color, 1)
            cv.putText(image, "{}: {}px".format(lab[1], Y), (X + W + lab_start, Y + 30), cv.FONT_HERSHEY_PLAIN, 1, color, 1)
            cv.putText(image, "{}: {}px".format(lab[2], W), (X + W + lab_start, Y + 50), cv.FONT_HERSHEY_PLAIN, 1, color, 1)
            cv.putText(image, "{}: {}px".format(lab[3], H), (X + W + lab_start, Y + 70), cv.FONT_HERSHEY_PLAIN, 1, color, 1)
        else:
            # Display custom text labels
            for i in range(len(text)):
                cv.putText(image, text[i].upper(), (X + W + lab_start, Y + 10 + (20 * i)), cv.FONT_HERSHEY_PLAIN, 1, color, 1)

# Define an empty main function (it can be extended for specific use cases)
def main():
    pass

# Entry point to the program
if __name__ == "__main__":
    main()
