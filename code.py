import numpy as np
import cv2
import time
import requests, datetime, sys


def video_upload():
    print("Uploading the file .......")
    filename = 'output_video.mp4'
    trigger_ = 'Trigger'
    cam_ = 'video'

    current_time = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
    url = 'http://13.58.60.237/upload.php'

    data = {
    'file': open(filename, 'rb')
    }

    time = {
    'ctime' : current_time,
    'cam' : cam_,
    'triggr' : trigger_
    }

    r = requests.post(url, files=data, data=time)
    print (r.text)

# Define the duration (in seconds) of the video capture here
capture_duration = 10

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output_video.mp4',fourcc, 20.0, (640,480))

start_time = time.time()
while( int(time.time() - start_time) <= capture_duration ):
    ret, frame = cap.read()
    if ret==True:
        print( int(time.time() - start_time))
        #frame = cv2.flip(frame,-1)
        # write the flipped frame
        out.write(frame)

        #cv2.imshow('frame',frame)
        #if cv2.waitKey(1) & 0xFF == ord('q'):
        #    break
    else:
        break

print("Done")
# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
video_upload()
