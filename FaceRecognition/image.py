#!/usr/bin/env python
#coding=utf8


import cv2
import os
from local_settings import *

class Image(object):
    def show(self, window, frame):
        cv2.imshow(window, frame)

    def save(self, filename, frame):
        cv2.imwrite(filename, frame)

    def read(self, filename, flags=None):
        if flags:
            return cv2.imread(filename, flags)
        else:
            return cv2.imread(filename)

    def cvt_color(self, frame, code):
        return cv2.cvtColor(frame, code)
        
    def face_roi(self, dst_filename, rect):
        img = cv2.cv.LoadImage('default.png')
        cv2.cv.SetImageROI(img, rect)
        cv2.cv.SaveImage(dst_filename, img)
        os.remove('default.png')

    def cut_face(self, filename):
        img = cv2.imread(filename, cv2.CV_LOAD_IMAGE_GRAYSCALE)
        classfier = cv2.CascadeClassifier(FACE_HAAR_PATH)
        cv2.equalizeHist(img, img)
        face_rect = classfier.detectMultiScale(img)
        return face_rect

    def resize(self, src, dsize):
        os.remove('cut.png')
        return cv2.resize(src, dsize)
        


