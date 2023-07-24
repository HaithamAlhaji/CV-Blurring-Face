import cv2
from cvzone.FaceDetectionModule import FaceDetector

# Initialize the video capture object to access the default camera (0).
cap = cv2.VideoCapture(0)

# Set the frame width and height of the video stream to 640x480 pixels.
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Create a FaceDetector object with a confidence threshold of 0.75.
dectector = FaceDetector(0.75)

# Start an infinite loop to process frames from the video stream.
while True:
    # Read a frame from the video stream.
    success, img = cap.read()

    # Use the FaceDetector to detect faces in the current frame.
    # The second argument, 'draw', is set to True, which means the bounding boxes around detected faces will be drawn on the 'img'.
    img, boxes = dectector.findFaces(img, True)

    # If there are detected faces (i.e., if 'boxes' is not empty):
    if boxes:
        # Iterate through each detected face and apply a blur effect to it.
        for i, box in enumerate(boxes):
            x, y, w, h = box["bbox"]

            # Ensure the coordinates are within the frame boundaries.
            if x < 0:
                x = 0
            if y < 0:
                y = 0

            # Crop the region of the face from the original image.
            imgCropped = img[y : y + h, x : x + w]

            # Apply a blur filter to the cropped face region.
            # The (35, 35) indicates the kernel size for the blur, which determines the amount of blurring.
            imgBlur = cv2.blur(imgCropped, (35, 35))

            # Replace the original face region with the blurred one.
            img[y : y + h, x : x + w] = imgBlur

    # Display the processed frame with possible blurred faces.
    cv2.imshow("Camera", img)

    # Wait for a key press and exit the loop if any key is pressed (waitKey(1) introduces a 1ms delay).
    cv2.waitKey(1)
