import mediapipe as mp
import cv2
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import numpy as np
import time
import keyboard  

current_gesture = None

model_path = 'gesture_recognizer.task'  

BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
VisionRunningMode = mp.tasks.vision.RunningMode


def print_result(result, output_image, timestamp_ms):
    global current_gesture
    if result.gestures:
        gesture = result.gestures[0][0].category_name
        

        if gesture != current_gesture:
            if gesture == 'Victory':
                for key in ['w', 'a', 's', 'd', 'space']:
                   keyboard.release(key)
                   current_gesture = None

            if current_gesture == 'Closed_Fist':
                keyboard.release('w')
            elif current_gesture == 'Open_Palm':
              keyboard.release('s')  
            elif current_gesture == 'Pointing_Up':
              keyboard.release('space')  
            elif current_gesture == 'Thumb_Up':
              keyboard.release('a') 
            elif current_gesture == 'Thumb_Down':
              keyboard.release('d')
        

        if gesture == 'Closed_Fist':
            keyboard.press('w')  # forward
        elif gesture == 'Open_Palm':
            keyboard.press('s')  # back
        elif gesture == 'Pointing_Up':
            keyboard.press('space')  # jump
        elif gesture == 'Thumb_Up':
            keyboard.press('a')  #left
        elif gesture == 'Thumb_Down':
            keyboard.press('d')  #right
        
        current_gesture = gesture


options = GestureRecognizerOptions(
    base_options=BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=print_result
)


recognizer = GestureRecognizer.create_from_options(options)

RECOGNITION_INTERVAL = 1
last_recognition_time = 0
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Webcam error")
        break

    frame_bgr = frame.copy()
    cv2.imshow("Webcam Feed", frame_bgr)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    current_time = time.time()

    if current_time - last_recognition_time >= RECOGNITION_INTERVAL:
 
        frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame_rgb)
        timestamp = int(current_time * 1000)

        recognizer.recognize_async(mp_image, timestamp)
        last_recognition_time = current_time
    
    
   

cap.release()
cv2.destroyAllWindows()
