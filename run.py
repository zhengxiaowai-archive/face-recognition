#!/usr/bin/env python2.7
#coding=utf8

from __future__ import print_function

import os
import cv2
import numpy as np
from FaceRecognition import *

from local_settings import *

def save_face(img, filename):
    # 获取人头位置
    try:
        position = img.cut_face('default.png')
        rect = tuple(position[0])
    except Exception, e:
        return ''
    
    img.face_roi('cut.png', rect)
    fina = img.resize(img.read('cut.png'), (100, 100))
    img.save('./images/%s.png' % filename, fina)
    return './images/%s.png' % filename

def show_rect(frame, classfier):
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
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0))

def show_text(frame, text, font, color):
    hight, width = frame.shape[:2]
    cv2.putText(frame, text, (hight / 2, width / 2), font, 1, color)

if __name__ == '__main__':
    cv2.namedWindow('watch')
    cap = Camera()
    img = Image()
    lbph = Recognition('lbph')
    classfier=cv2.CascadeClassifier(FACE_HAAR_PATH)
    model = False
    label, confidence = -1, 0.0

    while True:
        ok, frame = cap.read_frame()
        if not ok:
            print('cap dont work!')
            break

        show_text(frame, 'label: %s confidence: %s' % (str(label), str(confidence)), cv2.FONT_HERSHEY_SIMPLEX, (255, 0, 0))
        show_rect(frame, classfier)
        img.show('watch', frame)

        key = cv2.waitKey(10)
        ch = chr(key & 255)
        if ch in ['q', 'Q', chr(127)]:
            break
        if ch in [chr(13)]:
            student_number = input('请输入你的学号：')
            img.save('default.png', frame)
            filepath = save_face(img, '%d' % student_number)
            if not filepath:
                continue

            # 训练模型
            datas = []
            labels = []

            face = cv2.imread(filepath, cv2.CV_LOAD_IMAGE_GRAYSCALE)
            datas.append(np.array(face, 'uint8'))
            labels.append(int(student_number))

            if os.path.exists('./models/student.yml'):
                lbph.update(np.array(datas), np.array(labels))
            else:
                lbph.train(np.array(datas), np.array(labels))
            model = True
            lbph.save('./models/student.yml')
        
        if ch in [chr(32)]:
            # 识别模式
            label, confidence = -1, 0.0
            if not model:
                model = True
                lbph.load('./models/student.yml')
            img.save('default.png', frame)
            filepath = save_face(img, 'temp')
            if not filepath:
                continue

            face_data = cv2.imread(filepath, cv2.CV_LOAD_IMAGE_GRAYSCALE)
            face_data = cv2.equalizeHist(face_data)#灰度图像进行直方图等距化
            label, confidence = lbph.predict(face_data)
            os.remove('./images/temp.png')


    cap.destroy()
    cv2.destroyAllWindows()
