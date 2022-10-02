import cv2
import mediapipe as mp
import time



##to run the web cam
cap=cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands=mpHands.Hands()   #this object only uses rgb images
mpDraw=mp.solutions.drawing_utils
pTime=0
cTime=0

while True:
    success,img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    #print(results.multi_hand_landmarks)


    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id,lm in enumerate(handLms.landmark):
                # print(id,lm)
                h,w,c=img.shape

                cx,cy=int(lm.x*w),int(lm.y*h)  #multiply by height and width to get the value in pixels as its shown as a ratio of the picture
                print(id,cx,cy)
                # if id==0:
                #     cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)#the point on the bottom of the hand

                # if id==4:
                #     cv2.circle(img,(cx,cy),15,(255,0,255),cv2.FILLED)




            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS) ##i'm drawing on the img not rgb img because iam showing it


    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime


    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)


    cv2.imshow("Image",img)
    cv2.waitKey(1)