import cv2
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
vid=cv2.VideoCapture(0) #using your own camera
#img=cv2.imread('masks.jpg') #for using a photo
while True:
    _, img=vid.read()

    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.1,4)

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)  
    
    cv2.imshow('img',img)

    k=cv2.waitKey(30) & 0xff
    if k==27:
        break

    #cv2.waitKey() #for using a photo

vid.release()