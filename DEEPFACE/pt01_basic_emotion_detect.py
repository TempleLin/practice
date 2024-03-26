import cv2
import queue
from deepface import DeepFace

font = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10, 500)
fontScale = 1
fontColor = (0, 255, 0)
thickness = 1
lineType = 2
cap = cv2.VideoCapture(0)

emotion_text = "" #A global variable for emotion text
def emotion_detect(emotion_queue):
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        exit()

    try:
        while True:

            ret, frame = cap.read()
            if not ret:
                print("Error: Can't receive frame. Exiting ...")
                break

            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            # gray = cv2.cvtColor(face_cascade, cv2.COLOR_BGR2GRAY)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

            h, w, c = frame.shape

            try:
                analyze_result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
                emotion_text = analyze_result[0]['dominant_emotion']

                # Define the font and get the width and height of the frame.
                font = cv2.FONT_HERSHEY_SIMPLEX
                frame_height, frame_width = frame.shape[:2]

                # Calculate text width & height to draw the text in the top right corner.
                text_size = cv2.getTextSize(emotion_text, font, 1, 2)[0]
                text_x = frame_width - text_size[0] - 10  # 10 pixels from the right edge.
                text_y = text_size[1] + 10  # 10 pixels from the top.

                # Put the emotion text on the frame.
                cv2.putText(frame, emotion_text, (text_x, text_y), font, 1, (255, 255, 255), 2)
                
                cv2.imshow('Webcam Feed', frame)
                emotion_queue.put(emotion_text)
            except Exception as e:
                print("Error in emotion detection:", e)

            if cv2.waitKey(1) == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()
    