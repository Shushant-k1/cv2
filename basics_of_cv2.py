# show the  usage of imread and im write commad 
# esc key to cloase the window
# s key to save the file using imwrite



import cv2
img=cv2.imread("OIP.jpg")
cv2.imshow("image",img)
k=cv2.waitKey(0)
if k==27:
    cv2.destroyAllWindows()
elif k==ord("s"):
    cv2.imwrite("1.png",img)
    cv2.destroyAllWindows()

