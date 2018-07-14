import numpy as np
import cv2

def testCamera():

    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def testImage():
    im = cv2.imread('./test.jpg')
    cv2.imshow('spectrogram',im)
    print(type(im),im.shape)
    im_resize = cv2.resize(im,(300,300))
    print(type(im_resize), im_resize.shape)
    cv2.imshow('resize',im_resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # testCamera()
    testImage()

