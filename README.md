#TELLO FACE DETECTION

![Project Image](project_image.jpg)

## Table of Contents
- [Introduction](#introduction)
- [Key Features](#key-features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction

This project combines real-time face detection and annotation using the OpenCV library with the control of a DJI Tello drone. The integrated system captures video from a specified camera, detects faces in each frame, and adds various annotations to the detected faces, such as outlines, crosshairs, and labels. Additionally, it provides drone control capabilities to react to face movements.

Key elements of the project include:
- Face detection using Haar Cascade classifiers.
- Annotation of detected faces with frames, labels, and center points.
- Visualization of the drone's battery status.
- Drone control based on face position (commented out by default for safety).

## Key Features

- Real-time face detection in video streams.
- Annotation of detected faces for visualization.
- Integration with DJI Tello drone for controlling its movement.
- Battery status display.
- Highly customizable to adapt to specific use cases.

## Getting Started

### Prerequisites

To run this project, you'll need the following prerequisites:

- Python 3.x
- OpenCV (cv2)
- NumPy
- DJITelloPy (for drone control)

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/face-detection-drone-control.git
   ```

2. Navigate to the project directory:

   ```bash
   cd face-detection-drone-control
   ```

3. Install the required dependencies using pip:

   ```bash
   pip install opencv-python numpy djitellopy
   ```

## Usage

1. Ensure that the DJI Tello drone is connected and powered on.
2. Make sure the Haar Cascade XML file ("haarcascade_frontalface_default.xml") is present in the specified directory.
3. Run the project:

   ```bash
   python main.py
   ```

4. The system will start capturing video from the specified camera (camera index can be adjusted in the code).

## Customization

- To customize the behavior of the drone based on face position, uncomment and modify the relevant code section in the script.
- You can adjust the appearance of face annotations, labels, and frames by modifying the color and size parameters in the code.
- Explore the `faceDraw` class for more customization options.

## Contributing

Contributions to this project are welcome! Feel free to open issues, submit pull requests, or provide suggestions for improvements.

## License

This project is unlicensed and is considered to be in the public domain. You are free to use, modify, and distribute it without any legal restrictions. However, keep in mind that this means there are no warranties or guarantees associated with the project. Use it at your own discretion and responsibility.


## Acknowledgments

- Special thanks to Aleko Khomasuridze for the original code and idea.
```

This `README.md` file provides a detailed introduction to the project, instructions on how to get started, customize, and contribute. It also acknowledges the original author and provides a clear structure for potential contributors or users.
