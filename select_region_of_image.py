import cv2
img=cv2.imread("OIP.jpg")
roi=cv2.selectROI("hello",img,)
print(roi)
roi_crope=img[int(roi[1]):int(roi[1])+int(roi[3]),int(roi[0]):int(roi[0])+int(roi[2])]
cv2.imshow("hek",roi_crope)
cv2.imwrite("he.png",roi_crope)
cv2.waitKey(0)
cv2.destroyAllWindows()
