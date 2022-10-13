import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
size = (frame_width, frame_height)
result = cv2.VideoWriter('final.avi',
						cv2.VideoWriter_fourcc(*'MJPG'),
						10, size)
fondo=cv2.imread('./fondo1.jpg')
imagen_s=cv2.resize(fondo,(640,480))
while (True):
        ret, frame = cap.read()
        if ret ==False:
            break
        
        bgr = [97,181,147]
        trs = 50
        
        minBGR = np.array([bgr[0]-trs,bgr[1]-trs,bgr[2]-trs])
        maxBGR = np.array([bgr[0]+trs,bgr[1]+trs,bgr[2]+trs])
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
        
        if cv2.waitKey(1) & 0xFF==ord('c'):
            fondo=cv2.imread('./fondo2.jpg')
            imagen_s=cv2.resize(fondo,(640,480))
        
        if cv2.waitKey(1) & 0xFF==ord('b'):
            fondo=cv2.imread('./fondo1.jpg')
            imagen_s=cv2.resize(fondo,(640,480))
        
        result.write(total)
            
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
        
cap.release()
result.release()
cv2.destroyAllWindows()