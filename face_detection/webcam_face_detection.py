# import libraries
import cv2
# access webcam
cap=cv2.VideoCapture(0)  
face_cascade=cv2.CascadeClassifier('/home/sajmi/Desktop/BD_MAY/face_detection/data/haarcascade_frontalface_default.xml')
# read frames
while True:
    success,frame=cap.read()     
    grey_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # detect face in frames
    faces=face_cascade.detectMultiScale(grey_frame)
    print(len(faces))

    for (x,y,w,h) in faces:
         cv2.rectangle(frame,(x,y),(x+w,y+h),color=(0,255,0),thickness=3)
    # show detected face
         
    cv2.imshow('vedeo_capture',frame)
    if cv2.waitKey(1) & 0XFF==27:    
         break
cap.release()
cv2.destroyAllWindows()
