#!/usr/bin/env python2.7
#coding=utf8

import cv2

class Camera(object):
    def __init__(self, number=0):
        self._cap = cv2.VideoCapture(number)
    
    def read_frame(self):
        return self._cap.read()
    
    def save(self, frame, filename):
        cv2.imwrite()

    def destroy(self):
        self._cap.release()
