import cv2
img=cv2.imread("oipp.jpg")
cv2.imshow("image",img)
ret,thresh=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cannyimg=cv2.Canny(img,50,100)
cv2.imshow("canny",cannyimg)
cv2.imshow("threshol img",thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
