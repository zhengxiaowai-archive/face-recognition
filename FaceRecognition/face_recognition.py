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
            self._model = cv2.createFisherFaceRecognizer(threshold=1000)
        
        if face_type == 'lbph':
            self._model = cv2.createLBPHFaceRecognizer(threshold=100)

    def save(self, filename):
        self._model.save(filename)

    def load(self, filename):
        self._model.load(filename)

    def train(self, src, labels):
        self._model.train(src, labels)

    def update(self, src, labels):
        self._model.update(src, labels)

    def predict(self, src):
        return self._model.predict(src)
