#coding=utf8
from local_settings import *
import cv2
import numpy as np
import time
import os

def train_model(label):
    cv2.namedWindow("test")
    cap = cv2.VideoCapture(0)
    classfier=cv2.CascadeClassifier(FACE_HAAR_PATH)
    efr = cv2.createLBPHFaceRecognizer()
    n = 5
    while (n > 0):
        ok, frame = cap.read()
        if not ok:
            print 'camera read failed!'
            break;

        size=frame.shape[:2]#获得当前桢彩色图像的大小
        image=np.zeros(size,dtype=np.float16)#定义一个与当前桢图像大小相同的的灰度图像矩阵
        image = cv2.cvtColor(frame, cv2.cv.CV_BGR2GRAY)#将当前桢图像转换成灰度图像
        cv2.equalizeHist(image, image)#灰度图像进行直方图等距化

        #如下三行是设定最小图像的大小
        divisor=8
        h, w = size
        minSize=(w/divisor, h/divisor)
        faceRects = classfier.detectMultiScale(image, 1.2, 2, cv2.CASCADE_SCALE_IMAGE,minSize)

        if len(faceRects) > 0:
            labels = []
            datas = []
            for i, rect in enumerate(faceRects):
                if len(rect) > 0:
                    labels.append(2012132004)
                    datas.append(rect) 
                    
                    x, y, w, h = rect
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,0))
            efr.train(np.array(datas), np.array(label))
            efr.save('./models/%d.xml' % label)
        cv2.imwrite('./images/%d.png' % n, frame)
        cv2.imshow('test', frame)

        key=cv2.waitKey(10)
        c = chr(key & 255)
        if c in ['q', 'Q', chr(27)]:
            break
        n  = n -1
        time.sleep(0.1)
    cv2.destroyWindow("test")

def face_eigen_face_reconizer():
    model = cv2.createLBPHFaceRecognizer()
    datas = []
    labels = []
    for img in os.listdir('./images'):
        rect = cv2.imread(os.path.join('images',img), cv2.CV_LOAD_IMAGE_GRAYSCALE)
        datas.append(np.array(rect, 'uint8'))
        labels.append(2012132004)
    model.train(np.array(datas, 'uint8'), np.array(labels))
    model.save('me.xml')

def predict_face(label):

    cv2.namedWindow("test")
    cap = cv2.VideoCapture(0)
    classfier=cv2.CascadeClassifier(FACE_HAAR_PATH)
     
    model = cv2.createLBPHFaceRecognizer()
    #print mat_img
    model.load('./models/%d.xml' % label)

    while True:
        ok, frame = cap.read()
        if not ok:
            print 'camera read failed!'
            break;

        size=frame.shape[:2]#获得当前桢彩色图像的大小
        image=np.zeros(size,dtype=np.float16)#定义一个与当前桢图像大小相同的的灰度图像矩阵
        image = cv2.cvtColor(frame, cv2.cv.CV_BGR2GRAY)#将当前桢图像转换成灰度图像
        cv2.equalizeHist(image, image)#灰度图像进行直方图等距化

        #如下三行是设定最小图像的大小
        divisor=8
        h, w = size
        minSize=(w/divisor, h/divisor)
        faceRects = classfier.detectMultiScale(image, 1.2, 2, cv2.CASCADE_SCALE_IMAGE,minSize)

        if len(faceRects) > 0:
            for i, rect in enumerate(faceRects):
                if len(rect) > 0:
                    x, y, w, h = rect
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,0))
        cv2.imshow('test', frame)
        time.sleep(0.1) 
        cv2.imwrite('%d.png' % label, frame)
        print 'save a pic!!'
    
    
    
        #mat_img = cv2.imread('%d.png' % label,cv2.CV_LOAD_IMAGE_GRAYSCALE)
        mat_img = cv2.imread('./images/1.png',cv2.CV_LOAD_IMAGE_GRAYSCALE)
        label, confidence = model.predict(np.array(mat_img, 'uint8'))
        print label
        print confidence

        key=cv2.waitKey(10)
        c = chr(key & 255)
        if c in ['q', 'Q', chr(27)]:
            break
    cv2.destroyWindow("test")

if __name__ == '__main__':
    #train_model(2012132004)
    predict_face(2012132004)
