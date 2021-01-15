# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainProg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import cv2,os
import shutil
import csv
from mysql.connector.cursor import MySQLCursor
import numpy as np
from PIL import Image, ImageTk
from numpy.core.numeric import False_
import pandas as pd
import datetime
import time
import mysql.connector as mariadb

mydb_conn = mariadb.connect(host = "localhost", user = "root", passwd = "password", database = "facerecog_db")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1280, 694)
        MainWindow.setWhatsThis("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setInputMethodHints(QtCore.Qt.ImhNone)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 90, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 140, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 210, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 280, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 340, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(130, 610, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.lineEdit_ID = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ID.setGeometry(QtCore.QRect(200, 80, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_ID.setFont(font)
        self.lineEdit_ID.setWhatsThis("")
        self.lineEdit_ID.setAccessibleName("")
        self.lineEdit_ID.setAutoFillBackground(False)
        self.lineEdit_ID.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit_ID.setText("")
        self.lineEdit_ID.setObjectName("lineEdit_ID")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(200, 140, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setText("")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_classSec = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_classSec.setGeometry(QtCore.QRect(200, 210, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_classSec.setFont(font)
        self.lineEdit_classSec.setText("")
        self.lineEdit_classSec.setObjectName("lineEdit_classSec")
        self.lineEdit_timeStart = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_timeStart.setGeometry(QtCore.QRect(200, 270, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_timeStart.setFont(font)
        self.lineEdit_timeStart.setText("")
        self.lineEdit_timeStart.setObjectName("lineEdit_timeStart")
        self.lineEdit_timeEnd = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_timeEnd.setGeometry(QtCore.QRect(200, 330, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_timeEnd.setFont(font)
        self.lineEdit_timeEnd.setText("")
        self.lineEdit_timeEnd.setObjectName("lineEdit_timeEnd")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 20, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.btn_takeImg = QtWidgets.QPushButton(self.centralwidget)
        self.btn_takeImg.setGeometry(QtCore.QRect(220, 470, 280, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_takeImg.setFont(font)
        self.btn_takeImg.setObjectName("btn_takeImg")
        self.lineEdit_notif = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_notif.setGeometry(QtCore.QRect(250, 600, 851, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_notif.setFont(font)
        self.lineEdit_notif.setText("")
        self.lineEdit_notif.setObjectName("lineEdit_notif")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(690, 100, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.lineEdit_timeTrackRec = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_timeTrackRec.setGeometry(QtCore.QRect(850, 100, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_timeTrackRec.setFont(font)
        self.lineEdit_timeTrackRec.setText("")
        self.lineEdit_timeTrackRec.setObjectName("lineEdit_timeTrackRec")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(690, 50, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(520, 150, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(520, 220, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(520, 310, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.btn_trackAtn = QtWidgets.QPushButton(self.centralwidget)
        self.btn_trackAtn.setGeometry(QtCore.QRect(830, 150, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_trackAtn.setFont(font)
        self.btn_trackAtn.setObjectName("btn_trackAtn")
        self.btn_trainImg = QtWidgets.QPushButton(self.centralwidget)
        self.btn_trainImg.setGeometry(QtCore.QRect(200, 530, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_trainImg.setFont(font)
        self.btn_trainImg.setObjectName("btn_trainImg")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(190, 480, 20, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(180, 540, 16, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(1170, 100, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(690, 250, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(830, 290, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_search.setFont(font)
        self.btn_search.setObjectName("btn_search")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(40, 400, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.lineEdit_acyear = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_acyear.setGeometry(QtCore.QRect(190, 390, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_acyear.setFont(font)
        self.lineEdit_acyear.setText("")
        self.lineEdit_acyear.setObjectName("lineEdit_acyear")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(350, 400, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.lineEdit_sem = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_sem.setGeometry(QtCore.QRect(410, 390, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit_sem.setFont(font)
        self.lineEdit_sem.setText("")
        self.lineEdit_sem.setObjectName("lineEdit_sem")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.btn_takeImg.clicked.connect(self.takeImg)
        self.btn_trainImg.clicked.connect(self.trainImages)
        self.btn_trackAtn.clicked.connect(self.trackImages)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Face Recognition Attendance System"))
        self.label.setText(_translate("MainWindow", "ID no."))
        self.label_2.setText(_translate("MainWindow", "Full Name"))
        self.label_3.setText(_translate("MainWindow", "Class & Section"))
        self.label_4.setText(_translate("MainWindow", "Class Time Start"))
        self.label_5.setText(_translate("MainWindow", "Class Time End"))
        self.label_6.setText(_translate("MainWindow", "Notification:"))
        self.label_7.setText(_translate("MainWindow", "Register Student into Database"))
        self.btn_takeImg.setText(_translate("MainWindow", "Take Images for Database/ Update Section"))
        self.label_8.setText(_translate("MainWindow", "Class & Section"))
        self.label_9.setText(_translate("MainWindow", "Start Recording Attendance"))
        self.label_10.setText(_translate("MainWindow", "ex: John N Doe"))
        self.label_11.setText(_translate("MainWindow", "ex: COE510A"))
        self.label_12.setText(_translate("MainWindow", "24-hour format"))
        self.btn_trackAtn.setText(_translate("MainWindow", "Track Images (Record for Attendace)"))
        self.btn_trainImg.setText(_translate("MainWindow", "Train Images for Face Recognition"))
        self.label_13.setText(_translate("MainWindow", "1"))
        self.label_14.setText(_translate("MainWindow", "2"))
        self.label_15.setText(_translate("MainWindow", "ex: COE510A"))
        self.label_16.setText(_translate("MainWindow", "Search Student Attendance Status From Database"))
        self.btn_search.setText(_translate("MainWindow", "Database Attendace Search"))
        self.label_17.setText(_translate("MainWindow", "Academic Year"))
        self.label_18.setText(_translate("MainWindow", "Sem.:"))

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            pass
        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass
        return False
    
    def takeImg(self):        
        Id = self.lineEdit_ID.text()
        name = self.lineEdit_name.text()
        classSec=self.lineEdit_classSec.text()
        classStart = self.lineEdit_timeStart.text()
        classEnd = self.lineEdit_timeEnd.text()
        acadYr = self.lineEdit_acyear.text()
        sem = self.lineEdit_sem.text()
        mycursor = mydb_conn.cursor()
        sql = "SELECT name FROM tb_register WHERE class_id = '" + str(Id) + "' AND name = '" + name + "'"
        mycursor.execute(sql)
        result = mycursor.fetchone()
        sql1 = "SELECT class_sec from tb_studentsections WHERE class_id = '" + str(Id) + "' AND class_sec = '" + classSec + "'"
        mycursor.execute(sql1)
        result1 = mycursor.fetchone()
        mycursor.close()
        print(result)
        if not result and not result1:
            print('ahw')
            if(self.is_number(Id)):
                #cam = cv2.VideoCapture(0)
                cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
                harcascadePath = "haarcascade_frontalface_default.xml"
                detector=cv2.CascadeClassifier(harcascadePath)
                sampleNum=0
                while(True):
                    ret, img = cam.read()
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = detector.detectMultiScale(gray, 1.3, 5)
                    for (x,y,w,h) in faces:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
                        #incrementing sample number 
                        sampleNum=sampleNum+1
                        #saving the captured face in the dataset folder TrainingImage
                        cv2.imwrite("TrainingImage\ "+name +"."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                        #display the frame
                        cv2.imshow('frame',img)
                    #wait for 100 miliseconds 
                    if cv2.waitKey(100) & 0xFF == ord('q'):
                        break
                    # break if the sample number is morethan 60
                    elif sampleNum>60:
                        break
                cam.release()
                cv2.destroyAllWindows()
                res = "Images Saved for ID : " + Id + " Name : " + name + " Class-Sec : " + classSec
                #create database table
                tb_Id = str(Id)
                mycursor = mydb_conn.cursor() 
                sql = "INSERT INTO tb_register (class_id, name, date) SELECT * FROM (SELECT '"+str(Id)+"', '" + name + "', CURDATE()) AS tmp WHERE NOT EXISTS (SELECT class_id, name FROM tb_register WHERE class_id = '"+str(Id)+"' AND name = '" + name +"') LIMIT 1"
                mycursor.execute(sql)
                mydb_conn.commit()
                mycursor.close()
                mycursor = mydb_conn.cursor()
                sql1 = "INSERT INTO tb_studentsections (class_id, name, class_sec, classTimeStart, classTimeEnd, ac_year, sem) SELECT * FROM (SELECT '" + str(Id) + "', '" + name + "', '" + classSec + "', '" + classStart + "', '" + classEnd + "', '" + acadYr + "', '" + sem + "') AS tmp WHERE NOT EXISTS (SELECT class_id, class_sec FROM tb_studentsections WHERE class_id = '" + str(Id) + "' AND class_sec = '" + classSec + "') LIMIT 1"
                mycursor.execute(sql1)
                mydb_conn.commit()
                mycursor.close()
                row = [Id, name]
                with open('StudentDetails\StudentDetails.csv','a+') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(row)
                csvFile.close()
                self.lineEdit_notif.setText(res)
            #error message if ID is number or nut
            else:
                res = "ID has letters. Please entesr numeric ID number"
                self.lineEdit_notif.setText(res)
        if result and not result1:
            print('suc')
            mycursor = mydb_conn.cursor()
            sql = "INSERT INTO tb_studentsections (class_id, name, class_sec, classTimeStart, classTimeEnd, ac_year, sem) SELECT * FROM (SELECT '"+str(Id)+"', '"+name+"', '"+classSec+"', '"+classStart+"', '"+classEnd+"', '" + acadYr + "', '" + sem + "') AS tmp WHERE NOT EXISTS (SELECT class_id, class_sec FROM tb_studentsections WHERE class_id = '"+str(Id)+"' AND class_sec = '"+classSec+"') LIMIT 1"
            mycursor.execute(sql)
            mydb_conn.commit()
            mycursor.close()
            res = "Section Added for " + name 
            self.lineEdit_notif.setText(res)
            
    def trainImages(self):
        recognizer = cv2.face_LBPHFaceRecognizer.create()#recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector =cv2.CascadeClassifier(harcascadePath)
        faces,Id = self.getImagesAndLabels("TrainingImage")
        recognizer.train(faces, np.array(Id))
        recognizer.save("TrainingImageLabel\Trainner.yml")
        res = "Image Trained"#+",".join(str(f) for f in Id)
        self.lineEdit_notif.setText(res)

    #get images and corresponding ID
    def getImagesAndLabels(self, path):
        #get the path of all the files in the folder
        imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
        #print(imagePaths)
        
        #create empth face list
        faces=[]
        #create empty ID list
        Ids=[]
        #now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            #loading the image and converting it to gray scale
            pilImage=Image.open(imagePath).convert('L')
            #Now we are converting the PIL image into numpy array
            imageNp=np.array(pilImage,'uint8')
            #getting the Id from the image
            Id=int(os.path.split(imagePath)[-1].split(".")[1])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)        
        return faces, Ids
    
    def trackImages(self):
        recognizer = cv2.face.LBPHFaceRecognizer_create()#cv2.createLBPHFaceRecognizer()
        recognizer.read("TrainingImageLabel\Trainner.yml")
        harcascadePath = "haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(harcascadePath)
        df=pd.read_csv("StudentDetails\StudentDetails.csv")
        #cam = cv2.VideoCapture(0)
        cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        font = cv2.FONT_HERSHEY_SIMPLEX        
        col_names =  ['Id','Name','Class-Sec','Date','Time',]
        attendance = pd.DataFrame(columns = col_names)
        classSecVar = self.lineEdit_timeTrackRec.text()
        #data from trained images compared with camera capture
        #then display ID and name on window    
        while True:
            ret, im =cam.read()
            gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
            faces=faceCascade.detectMultiScale(gray, 1.2,5)
            mycursor = mydb_conn.cursor()    
            for(x,y,w,h) in faces:
                cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
                Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
                global date        
                global timeStamp                           
                if(conf < 50):
                    ts = time.time()      
                    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                    aa=df.loc[df['Id'] == Id]['Name'].values
                    #ab=df.loc[df['Id'] == Id]['Class-Sec'].values
                    aa_name = str(aa).strip('[]')
                    #ab_classSec = str(ab).strip('[]')
                    aa_namer= aa_name.replace("'","")
                    #ab_classSecr = ab_classSec.replace("'","")
                    attendance.loc[len(attendance)] = [Id,aa_namer.strip(),classSecVar,date,timeStamp]
                    tt=str(Id)+"-"+aa_namer.strip()+"-"+classSecVar
                    #classSecstr = ab_classSecr.strip()
                #display unknown if unknown face    
                else:
                    Id='Unknown'                
                    tt=str(Id)
                #save unknown image  
                if(conf > 75):
                    noOfFile=len(os.listdir("ImagesUnknown"))+1
                    cv2.imwrite("ImagesUnknown\Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])            
                cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)
                sql = "SELECT sec_id, classTimeStart, classTimeEnd, ac_year, sem FROM tb_studentsections WHERE class_id = '"+str(Id)+"' AND class_sec = '"+classSecVar+"' LIMIT 1"
                mycursor.execute(sql)
                result = mycursor.fetchone()
                if result:
                    secId = result[0]
                    start = str(result[1])
                    end = str(result[2])
                    acadYr = result[3]
                    sem = result[4]
                    sql1 = "INSERT INTO tb_records (class_id, name, class_sec, sec_id, date, time_record, classTimeStart, classTimeEnd, timeOffset, status_preslate, ac_year, sem) SELECT * FROM (SELECT '" + str(Id) + "', '" + aa_namer.strip() + "', '" + classSecVar + "', '" + str(secId) + "', '" + date + "', '" + timeStamp + "', '"+start+"', '"+end+"', ADDTIME('"+start+"',1000), 'initial_rec', '" + acadYr + "', '" + str(sem) + "') AS tmp WHERE NOT EXISTS (SELECT class_id, class_sec, date FROM tb_records WHERE class_id = '"+str(Id)+"' AND class_sec = '"+classSecVar+"' AND date = '" + date + "') LIMIT 1"
                    mycursor.execute(sql1)
                    mydb_conn.commit()
                    sql2 = "UPDATE tb_records SET status_preslate = CASE WHEN time_record < classTimeStart THEN 'present' WHEN time_record > timeOffset THEN 'late' WHEN time_record >= classTimeStart THEN 'present' WHEN time_record >= classTimeEnd THEN 'invalid-time-in' ELSE NULL END WHERE class_id = '"+str(Id)+"' AND class_sec = '"+classSecVar+"' AND status_preslate = 'initial_rec' AND date = '"+date+"' LIMIT 1"
                    mycursor.execute(sql2)
                    mydb_conn.commit()
            attendance=attendance.drop_duplicates(subset=['Id'],keep='first')
            cv2.imshow('im',im)
            if (cv2.waitKey(1)==ord('q')):
                mycursor.close()
                cam.release()
                cv2.destroyAllWindows()
                break
        #save attendance of detected faces into csv file
        ts = time.time()      
        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        Hour,Minute,Second=timeStamp.split(":")
        fileName="Attendance\Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
        attendance.to_csv(fileName,index=False)
        #print(attendance)
        res=attendance 
        self.lineEdit_notif.setText(res)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
