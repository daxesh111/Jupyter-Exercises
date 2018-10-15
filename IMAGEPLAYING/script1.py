import cv2
img = cv2.imread("galaxy.jpg",0)
print(img)
print(len(img))


resized_img = cv2.resize(img,(1378,720))
cv2.imshow("Daxesh", resized_img)
cv2.waitKey(0)
cv2.destroyAllwindows()
