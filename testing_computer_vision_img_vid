import cv2 as cv

#img = cv.imread('hari.jpg')
#cv.imshow('myself', img)
#cv.waitKey(0)

capture = cv.VideoCapture('trump.mp4')


while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0XFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
