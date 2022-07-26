import 

img=cv2.imread("oipp.jpg")
cv2.imshow("image",img)
# can change the value and play with different numbers
# for max sharpness set [1,1] to camparable max value
k_sharpene=np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
sharpened=cv2.filter2D(img,-1,k_sharpene)
cv2.imshow("shar",sharpened)
cv2.waitKey(0)
cv2.destroyAllWindows()
