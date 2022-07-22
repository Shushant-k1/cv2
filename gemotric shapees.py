import cv2
import numpy as np
# for image
#img=cv2.imread("OIP.jpg",1)
# for black image using numpy
img=np.zeros([512,512,3],np.uint8)
img=cv2.arrowedLine(img,(0,0),(155,155),(146,96,3),5)
img=cv2.arrowedLine(img,(155,0),(0,155),(146,96,3),5)
img=cv2.rectangle(img,(0,0),(155,155),(146,96,3),5)
font=cv2.FONT_HERSHEY_SIMPLEX
img=cv2.circle(img,(40,40),40,(146,10,4),2)
img=cv2.putText(img,"hello",(40,100),font,1,(255,2,4),2,cv2.LINE_AA)
cv2.imshow("shushant",img)
cv2.waitKey()
cv2.destroyAllWindows()
