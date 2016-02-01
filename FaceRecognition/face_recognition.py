#!/usr/bin/env python2.7
# coding=utf8

from __future__ import print_function

import cv2
import numpy as np
import os
import glob
import time

from local_settings import *

class Recognition(object):
    def __init__(self, face_type):
        self._type = ['eigen', 'fisher', 'lbph']
        if face_type not in self._type:
            raise ValueError("you must be chose in ['eigen', 'fisher', 'lbph']")
        
        if face_type == 'eigen':
            self._model = cv2.createEigenFaceRecognizer(threshold=1000)
        
        if face_type == 'fisher':
            self._model = cv2.createEigenFaceRecognizer(threshold=1000)
        
        if face_type == 'lbph':
            self._model = cv2.createEigenFaceRecognizer(threshold=100)

    def save(self, filename):
        self._model.save(filename)

    def load(self):
        self._model.load(filename)

    def train(self, src, labels):
        self._mode.train(src, labels)

    def predict(self, src):
        return self._mode.predict(src)






#    def take_photos(self, window_name):
#        cv2.namedWindow(window_name)
#        cap = cv2.VideoCapture(0)
#        #model = cv2.createEigenFaceRecognizer()
#        
#        label = input('please input your number :')
#        
#        press_count = 0
#        while True:
#            ok, frame = cap.read()
#            if not ok:
#                print('camera can not work, please check it!')
#                break
#            else:
#
#                cv2.imshow(window_name, frame)
#                
#                key = cv2.waitKey(10)
#                ch = chr(key & 255)
#                if ch in ['q', 'Q', chr(127)]:
#                    break
#                if ch in [chr(13)]:
#                    press_count = press_count + 1
#                    print('saving!!!')
#                    if not os.path.exists('./images/%d' % label):
#                        os.makedirs('./images/%d' % label, mode=0755)
#                    cv2.imwrite(os.path.join('./images/%d' % label,'%d.png' % press_count), 
#                            frame)
#                    if press_count == 3:
#                        break
#
#        cv2.destroyWindow(window_name)
#
#    def train(self, dirpath):
#        datas = []
#        labels = []
#        #model = cv2.createEigenFaceRecognizer()
#        basedir = os.path.basename(dirpath)
#
#        for img in self._iglob(dirpath, '*.png'):
#            face = cv2.imread(img, cv2.CV_LOAD_IMAGE_GRAYSCALE)
#            datas.append(np.array(face, 'uint8'))
#            labels.append(int(basedir))
#        self.model.train(np.array(datas, 'uint8'), np.array(labels))
#        self.model.save('./models/%s.xml' % basedir)
#        print('trained!!!, save in ./models')
#
#    def _iglob(self, dirpath, wildcard):
#        '''
#            _iglob(dirpath, wildcard) -> gen
#        '''
#        return glob.iglob(os.path.join(dirpath, wildcard))
#        
#    def predict(self, picture, modelxml):
#        #model = cv2.createEigenFaceRecognizer()
#        print(modelxml)
#        self.model.load(modelxml)
#        mat_img = cv2.imread(picture, cv2.CV_LOAD_IMAGE_GRAYSCALE)
#        label, confidence = self.model.predict(np.array(mat_img, 'uint8'))
#        print(label)
#        print(confidence)
#
#    def watch(self):
#        self.model.load('./models/2.xml')
#        cv2.namedWindow('watch')
#        cap = cv2.VideoCapture(0)
#
#        while True:
#            ok, frame = cap.read()
#            if not ok:
#                print('cap dont work!')
#                break
#            image = cv2.cvtColor(frame, cv2.cv.CV_BGR2GRAY)
#            label, confidence = self.model.predict(np.array(image, 'uint8'))
#            cv2.imshow('watch', frame)
#            print(label)
#            print(confidence)
#            print('===========')
#    
#        cv2.destroyWindow('watch')
#




