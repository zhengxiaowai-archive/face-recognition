#!/usr/bin/env python2.7
#coding=utf8

from __future__ import print_function

import cv2
import numpy as np
from FaceRecognition import *

if __name__ == '__main__':
    cv2.namedWindow('watch')
    cap = Camera()
    img = Image()
    lbph = Recognition('lbph')
    while True:
        ok, frame = cap.read_frame()
        if not ok:
            print('cap dont work!')
            break
        img.show('watch', frame)

        key = cv2.waitKey(10)
        ch = chr(key & 255)
        if ch in ['q', 'Q', chr(127)]:
            break
        if ch in [chr(13)]:
            img.save('default.png', frame)
            print('save a image')

            # 获取人头位置
            position = img.cut_face('default.png')
            img.face_roi('cut.png', tuple(position[0]))
            fina = img.resize(img.read('cut.png'), (100, 100))
            img.save('./images/hexiangyu.png', fina)
            #image = img.cvt_color(frame, cv2.cv.CV_BGR2GRAY)
            #lbph.train(np.array(image), np.array([2012132004]))
            break
    

    cap.destroy()
    cv2.destroyAllWindows()



    #f = FaceRecognition()
    #f.take_photos('test')
    #f.train('./images/2')
    #f.predict('3.png', './models/2.xml')
    #f.watch()
