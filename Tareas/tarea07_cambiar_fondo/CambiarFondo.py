# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cv2
import numpy as np

# Video de entrada
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
fondo=cv2.imread('E:\\UDG Kevin\\Semestre 3\\Sem. Algoritmia\\Programas\\Cambiar Fondo\\1.jpg')
imagen_s=cv2.resize(fondo,(640,480))
while (True):
        ret, frame = cap.read()
        if ret ==False:
            break
        
        bgr = [30,204,73]
        thresh = 95   

        minBGR = np.array([bgr[0] - thresh, bgr[1] - thresh, bgr[2] - thresh])
        maxBGR = np.array([bgr[0] + thresh, bgr[1] + thresh, bgr[2] + thresh])
        maskBGR = cv2.inRange(frame,minBGR,maxBGR)
        mask_inv = cv2.bitwise_not(maskBGR)
        cv2.imshow('mascara',maskBGR)
        cv2.imshow('mascara_inv',mask_inv)

        resultBGR = cv2.bitwise_and(frame,frame, mask=mask_inv)

        result_inv = cv2.bitwise_and(imagen_s, imagen_s, mask = maskBGR)

        total=cv2.add(resultBGR,result_inv)

        cv2.imshow('resultado',total)
        cv2.imshow('Fondo', imagen_s)

        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
        
cap.release()
cv2.destroyAllWindows()