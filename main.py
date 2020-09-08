import cv2

#img=cv2.imread("galaxy.jpg",0)
#print(img.ndim)
#print(img.shape)
#resized_image=cv2.resize(img,(int(img.shape[0]/2),int(img.shape[1]/2))
#opens a window named gaalxy and destroys the window after 2 seconds 
#cv2.imshow("Galaxy", resized_image)
#cv2.imwrite("Galaxyresize.jpg", resized_image)
#cv2.waitKey(2000)
#cv2.destroyAllWindows()

#reads in a cascades, these are xml files which contain features of the face

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("photo.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#creating a face object where we want to detect the starting point of
#the face and then draw a sqaure around the face

#scalefactor is what python scales the image when searching. The smaller the value the more accurate
faces=face_cascade.detectMultiScale(gray_img, 
scaleFactor=1.05,
minNeighbors=5)


for x,y,width,height in faces: 
    img =cv2.rectangle(img,(x,y),(x+width,y+height),(0,255,0),3)


cv2.imshow("Galaxy", img)
cv2.waitKey(0)
cv2.destroyAllWindows()