"""Created by Enigma for Dexterix Hackathon 2018"""

#importing all the modules for recognition
import cv2, numpy as np
import xlwrite
import time
start=time.time()
period=8
face_cas = cv2.CascadeClassifier('haarcascade_profileface.xml')
cap = cv2.VideoCapture(0)
recognizer = cv2.face.LBPHFaceRecognizer_create()

#reading from the trainer.yml file
recognizer.read('trainer/trainer.yml')

id=0
filename='filename'
dict = {
            'item1': 1
}

#Setting up the font
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cas.detectMultiScale(gray, 1.3, 7)
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)
        id,conf=recognizer.predict(roi_gray)

        if id==1:
            id='Aditya Verma'
            if (str(id)) not in dict:
                filename=xlwrite.output('attendance','BCA',1,id,'yes')
                dict[str(id)]=str(id)
                
        elif id==2:
            id = 'Ashish Yadav'
            if (str(id)) not in dict:
                filename =xlwrite.output('attendance', 'BCA', 2, id, 'yes')
                dict[str(id)] = str(id)
                
        elif id==3:
            id = 'Mayank Chauhan'
            if (str(id)) not in dict:
                filename =xlwrite.output('attendance', 'BCA', 3, id, 'yes')
                dict[str(id)] = str(id)

        elif id==4:
            id = 'Muzammil Ansari'
            if (str(id)) not in dict:
                filename =xlwrite.output('attendance', 'BCA', 4, id, 'yes')
                dict[str(id)] = str(id)

        elif id==5:
            id = 'Sachin Kumar'
            if (str(id)) not in dict:
                filename =xlwrite.output('attendance', 'BCA', 5, id, 'yes')
                dict[str(id)] = str(id)
 
        #Displaying Text In The Rectangle while recognizing the face.
        cv2.putText(img,str(id)+" "+str(conf),(x,y-10),font,0.55,(120,255,120),1)
        
    cv2.imshow('frame',img)
    
    if time.time()>start+period:
        break
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
