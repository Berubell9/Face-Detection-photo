imagePath = r'img.jpg'
cascPath = "haarcascade_frontalface_default.xml"

import cv2  
img = cv2.imread('img.jpg')#เเปลงจาก ImagePath ให้ใส่ในตัวเเปล img
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')#เเปลงตรวจจับใบหน้าให้อยู่ใน face_cascade
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#แปลงรูปเป็นขาวดำ

faces = face_cascade.detectMultiScale(gray, 1.3)#ใช้ haar cascade ตรวจจับใบหน้า
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)#กรอบสีเขียว
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

cv2.imshow('img.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()