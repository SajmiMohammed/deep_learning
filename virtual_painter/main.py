
import cv2
import HandTrackingModule as htm
import numpy as np


detector = htm.handDetector()
draw_color=(0,0,255)
#creating image canvas
img_canvas= np.zeros((500,1200,3),np.uint8) #creating rgb color zero matrix canvas
cap=cv2.VideoCapture(0)  

while True:
    x,img=cap.read()   
    img=cv2.resize(img,(1200,500)) #resizing the frame that display
    #resize the window only that we can draw 5 rect in same line 
    # drawing rectangle and adding text
    img=cv2.flip(img,1)#flipping the screen
    
    #draw rectangles
    img=cv2.rectangle(img,(10,100),(200,10),(255,0,0),-1)#blue
    img=cv2.rectangle(img,(210,100),(400,10),(0,0,255),-1)#red
    img=cv2.rectangle(img,(410,100),(600,10),(0,255,0),-1)#green
    img=cv2.rectangle(img,(610,100),(800,10),(0,255,255),-1)#yellow
    img=cv2.rectangle(img,(810,100),(1250,10),(255,255,255),-1)#white
    img=cv2.putText(img,text='ERASER',org=(900,60),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=1,color=(0,0,0),thickness=3)
    
    
    #detect hands
    img = detector.findHands(img,)
    lmlist = detector.findPosition(img)
     
    if len(lmlist)!=0:
        x1,y1 = lmlist[8][1:] #index finger tip coordinate
        x2,y2 = lmlist[12][1:] #middle finger tip coordinate
        
        
    #detect if fingers are up
        fingers = detector.fingersUp()  #1==>up ,0=>down
        #print(fingers)
    
    
    #check if two fingers are up --selection mode
        if fingers[1] and fingers[2]:
           # print('selection mode')
            xp , yp = 0 , 0
            
            if y1<100:
                if 210<=x1<=410:
                    print('red')
                    draw_color=(0,0,255)
                elif 10<=x1<=210:
                    print('blue')
                    draw_color=(255,0,0)
                elif 410<=x1<=610:
                    print('green')
                    draw_color=(0,255,0)
                elif 610<=x1<=810:
                    print('yellow')
                    draw_color=(0,255,255)
                elif 810<=x1<=1250:
                    print('eraser')
                    draw_color=(0,0,0)
            cv2.rectangle(img,(x1,y1),(x2,y2),color=draw_color,thickness=-1)
    
    #check if index finger is up --drawing mode
        if fingers[1] and not fingers[2]:
            cv2.circle(img,(x1,y1),15,draw_color,thickness=-1)
            #print('drawing mode')
            
            
            if xp==0 and yp==0:
                xp=x1
                yp=y1
            
            
            #colors
            if draw_color==(0,0,0):
                cv2.line(img,(xp,yp),(x1,y1),color=draw_color,thickness=50)
                cv2.line(img_canvas,(xp,yp),(x1,y1),color=draw_color,thickness=50)

            else:
                cv2.line(img,(xp,yp),(x1,y1),color=draw_color,thickness=7)
                cv2.line(img_canvas,(xp,yp),(x1,y1),color=draw_color,thickness=7)
                
            xp,yp=x1,y1
            
            
    img_grey = cv2.cvtColor(img_canvas,cv2.COLOR_BGR2GRAY)
    _ , img_inv = cv2.threshold(img_grey,20,255,cv2.THRESH_BINARY_INV)
    img_inv = cv2.cvtColor(img_inv,cv2.COLOR_GRAY2BGR)
    
    img = cv2.bitwise_and(img,img_inv)
    img = cv2.bitwise_or(img,img_canvas)
    
    img = cv2.addWeighted(img,1,img_canvas,0.5,0)
    
    cv2.imshow('virtual_painter',img)
    
    
    
    if cv2.waitKey(1) & 0XFF==27:    
         break
cap.release()
cv2.destroyAllWindows()
        
              
             
         