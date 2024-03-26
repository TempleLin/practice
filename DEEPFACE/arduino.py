import serial  
import queue
import sys
import threading
from time import sleep
import pt01_basic_emotion_detect

COM_PORT = 'COM9'
BAUD_RATES = 9600
ser = serial.Serial(COM_PORT, BAUD_RATES)


try:
    emotion_queue = queue.Queue()
    emotion_machine = threading.Thread(target=pt01_basic_emotion_detect.emotion_detect,args=(emotion_queue,))
    emotion_machine.daemon = True 
    emotion_machine.start()
except KeyboardInterrupt:
    print("stop")



try:
    while True:
        emotion_type = emotion_queue.get()

        if emotion_type == 'angry':
            print('angry')
            ser.write(b'0\n')  
            sleep(0.5)     
        elif emotion_type == 'disgust':
            print('disgust')
            ser.write(b'1\n')
            sleep(0.5)
        elif emotion_type == 'fear':
            print('fear')
            ser.write(b'2\n')
            sleep(0.5)
        elif emotion_type == 'happy':
            print('happy')
            ser.write(b'3\n')
            sleep(0.5)
        elif emotion_type == 'sad':
            print('sad')
            ser.write(b'4\n')
            sleep(0.5)
        elif emotion_type == 'neutral':
            print('neutral')
            ser.write(b'5\n')
            sleep(0.5)
        elif emotion_type == 'surprise':
            print('surprise')
            ser.write(b'6\n')
            sleep(0.5)
            
except KeyboardInterrupt:
    ser.close()
    print('再見！')

