import cv2
import numpy as np

class GameObjectDetector:
    def __init__(self, model_path):
        self.model = cv2.dnn.readNetFromONNX(model_path)

    def detect_objects(self, image):
        blob = cv2.dnn.blobFromImage(image, 1/255.0, (224, 224), swapRB=True, crop=False)
        self.model.setInput(blob)
        detections = self.model.forward()
        return detections

# Example usage
if __name__ == "__main__":
    detector = GameObjectDetector('path_to_your_model.onnx')
    image = cv2.imread('game_screen.png')  # Replace with actual game screen
    detections = detector.detect_objects(image)
    print(detections)