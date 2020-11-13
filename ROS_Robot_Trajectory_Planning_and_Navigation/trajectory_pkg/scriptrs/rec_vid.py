#!/usr/bin/env python
import numpy as np
import cv2

def video_record():
    cap = cv2.VideoCapture(0)
    fourcc = cv2.cv.CV_FOURCC(*'XVID')
    out = cv2.VideoWriter('data_files/video/output.avi', fourcc, 20.0, (640, 480))

    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            # frame = cv2.flip(frame,0)
            out.write(frame)

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

################################################

if __name__ == "__main__":
    try:
        video_record()
    except KeyboardInterrupt:
        print ("---Video Recording Stopped---")
