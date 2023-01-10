import cv2
import mediapipe

from utils.dataset_utils import load_dataset, load_reference_signs
from utils.mediapipe_utils import mediapipe_detection
from sign_recorder import SignRecorder


def preproceso():
    videos = load_dataset()
    print('doing something3')
    # Create a DataFrame of reference signs (name: str, model: SignModel, distance: int)
    reference_signs = load_reference_signs(videos)
    print('doing something4')
    # Object that stores mediapipe results and computes sign similarities
    sign_recorder = SignRecorder(reference_signs)
    print('doing something5')
    return  sign_recorder


def proceso(sign_recorder):
    print("preprocess started")
    # Turn on the webcam
    #cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    c = 0
    cap = cv2.VideoCapture('fname.mp4')
    # Set up the Mediapipe environment
    with mediapipe.solutions.holistic.Holistic(
        min_detection_confidence=0.5, min_tracking_confidence=0.5
    ) as holistic:
            # Read feed
            ret = True
            recorded_results = []
            while ret:
                # Read feed
                ret, frame = cap.read()
                if ret == True:
                    print('frames counted:'+ str(c))
                    # Make detections
                    image, results = mediapipe_detection(frame, holistic)
                    # Process results
                    recorded_results.append(results)
                    c = c+1
            sign_detected, is_recording = sign_recorder.process_video(recorded_results)
            print("preprocess finished")
            return sign_detected