import cv2
import numpy as np
import sqlite3


faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture(0);

def insertOrUpdate(Id,Name,Age,Gen,Cgpa):
    conn=sqlite3.connect("FaceBase.db")
    cmd="SELECT * FROM People WHERE ID="+str(Id)
    cursor=conn.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cmd="UPDATE People SET Name="+str(Name)+"WHERE ID="+str(Id)
    else:
        cmd="INSERT INTO People(ID,Name,Age,Gender,Cgpa) Values("+str(Id)+","+str(Name)+","+str(Age)+","+str(Gen)+","+str(cgpa)+")"
    conn.execute(cmd)
    conn.commit()
    conn.close()



id=raw_input('enter user id')
name=raw_input('enter the name')
age=raw_input('enter the age')
gen=raw_input('enter the gender')
cgpa=raw_input('enter the cgpa')
insertOrUpdate(id,name,age,gen,cgpa)
sampleNum=0;



while(True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        sampleNum=sampleNum+1;
        cv2.imwrite("dataset/User."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x-50,y-50),(x+w+50,y+h+50),(255,0,0),2)
        cv2.waitKey(100);
    cv2.imshow("Face",img);
    cv2.waitKey(100);
    if(sampleNum>50):
        break;
cam.release()
cv2.destroyAllWindows()
