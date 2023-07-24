# Blurring Face

![](https://github.com/HaithamAlhaji/CV-Truck-Stop/blob/main/footages/result.gif)

This is a simple Python application that captures video from the default camera, detects faces in the frames using OpenCV and the cvzone library, and then applies a blur effect to the detected faces. The application continuously processes frames and displays the video stream with any detected faces blurred in real-time.

## Installation

To run this application, you need to have Python installed on your system. You also need to install the required libraries using pip.

1. **Install Python:** If you don't have Python installed, download and install the latest version from the official Python website: [python.org](https://www.python.org/downloads/)

2. **Install the required libraries:** Open a terminal or command prompt and run the following command to install the necessary libraries:
   pip install opencv-python cvzone

## Usage

1. Clone the repository or download the files to your local machine.

2. Open a terminal or command prompt and navigate to the directory containing the downloaded files.

3. Run the `blurring_face.py` script using Python:

python blurring_face.py

4. The application will start capturing video from your default camera and displaying it in a new window.

5. As faces are detected in the video stream, they will be automatically blurred in real-time.

6. To exit the application, simply close the video window or press any key in the terminal or command prompt.

## Notes

- This application uses the `cvzone` library, which provides the FaceDetectionModule for face detection. Make sure you have installed this library along with its dependencies before running the script.

- If you have multiple cameras connected to your system, the application will use the default camera (index 0) by default. If you want to use a different camera, you can modify the `cap = cv2.VideoCapture(0)` line in the `blurring_face.py` script and change the camera index accordingly (e.g., `cap = cv2.VideoCapture(1)` for the second camera).

- The application might not be perfectly accurate in detecting faces, especially under challenging lighting conditions or with partial occlusion. Depending on your use case, you may want to explore more advanced face detection methods or modify the code to improve accuracy.

## Acknowledgments

- The `cvzone` library used in this project is developed by [Murtaza's Workshop](#). It provides convenient wrappers around OpenCV functions for computer vision tasks.

- This project is inspired by various OpenCV tutorials and examples available online. Special thanks to the OpenCV community for their valuable contributions to computer vision.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
