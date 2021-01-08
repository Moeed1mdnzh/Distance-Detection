import serial,cv2
import numpy as np
 
arduinoSerialData = serial.Serial('COM4',9600)
cap = cv2.VideoCapture(1)
face_cascade = cv2.CascadeClassifier("face.xml")
 
while True:
    success,img = cap.read()
    if success:
        shape = img.shape[:2][::-1]
        shape = shape[0]//2,shape[1]//2
        if (arduinoSerialData.inWaiting()>0):
            dist = arduinoSerialData.readline().decode("utf-8").strip("\n")
            dist = float(dist.strip("\r"))
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            face = face_cascade.detectMultiScale(gray,1.3,5)
            for x,y,w,h in face:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),4)
                x_mean = int(np.array(range(x,x+w)).mean())
                y_mean = int(np.array(range(y,y+h)).mean())
                cv2.line(img,(x_mean,y_mean),shape,(255,255,255),5)
                cv2.circle(img,shape,5,(0,255,255),-1)
                cv2.circle(img,(x_mean,y_mean),5,(0,255,255),-1)
                cv2.putText(img,f"Distance : {dist}",(20,30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),4)
            cv2.imshow("Frame",img)
            if cv2.waitKey(1) == ord("q"):
                break
                                    
    else:
        print("Could not turn on your webcam successfully")
        break

cv2.destroyAllWindows()
cap.release()
    
