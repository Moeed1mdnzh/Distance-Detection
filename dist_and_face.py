import cv2
import numpy as np 

cap = cv2.VideoCapture(2,cv2.CAP_DSHOW)
faces = cv2.CascadeClassifier("face.xml")

while True:
	_,img = cap.read()
	img = cv2.flip(img,1)
	shape = img.shape[:2][::-1]
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	face = faces.detectMultiScale(gray,1.3,5)
	for x,y,w,h in face:
		lengths = []
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),7)
		face_x = x+(w//2)
		face_y = y+(h//2)
		win_cord = [[0,0],[shape[0],0],[0,shape[1]],[shape[0],shape[1]]]
		vectors = [[x-win_cord[0][0],y-win_cord[0][1]],[(x+w)-win_cord[1][0],y-win_cord[1][1]],
		[x-win_cord[2][0],(y+h)-win_cord[2][1]],[(x+w)-win_cord[3][0],(y+h)-win_cord[3][1]]]
		for vector in vectors:
			lengths.append(np.sqrt((vector[0]**2)+(vector[1]**2)))
		lengths = np.array(lengths)
		dist = round((lengths.mean()*2)/10,1)
		cv2.line(img,(face_x,face_y),(shape[0]//2,shape[1]//2),(255,255,255),5)
		cv2.circle(img,(shape[0]//2,shape[1]//2),5,(0,255,255),-1)
		cv2.circle(img,(face_x,face_y),5,(255,0,255),-1)
		pts = [[face_x,shape[0]],[face_y,shape[1]]]
		dist_cord = np.array(range(min(pts[0]),max(pts[0]))).mean(),np.array(range(min(pts[1]),max(pts[1]))).mean()
		dist_cord = list(dist_cord)
		dist_cord[0],dist_cord[1] = int(dist_cord[0]),int(dist_cord[1])
		cv2.putText(img,f"{dist}",tuple(dist_cord),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),4)
	cv2.imshow("unnamed",img)
	key = cv2.waitKey(1) & 0xff
	if key == ord("q"):
		break

cv2.destroyAllWindows()
cap.release()