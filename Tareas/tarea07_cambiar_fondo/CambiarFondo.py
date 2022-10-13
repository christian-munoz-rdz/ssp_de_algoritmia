import cv2
import numpy as np

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
frame_width = int(video.get(3))
frame_height = int(video.get(4))
size = (frame_width, frame_height)
exportable = cv2.VideoWriter('final.avi',
						cv2.VideoWriter_fourcc(*'MJPG'),
						10, size)
fondo=cv2.imread('./fondo1.jpg')
fondo=cv2.resize(fondo,(640,480))
while (True):
        ret, frame = video.read()
        if ret ==False:
            break
        
        bgr = [97,181,147]
        trs = 50
        
        low = np.array([bgr[0]-trs,bgr[1]-trs,bgr[2]-trs])
        high = np.array([bgr[0]+trs,bgr[1]+trs,bgr[2]+trs])
        mask = cv2.inRange(frame,low,high)
        mask_inv = cv2.bitwise_not(mask)
        cv2.imshow('mascara',mask)
        cv2.imshow('mascara_inv',mask_inv)

        result = cv2.bitwise_and(frame,frame, mask=mask_inv)

        result_inv = cv2.bitwise_and(fondo, fondo, mask = mask)

        total=cv2.add(result,result_inv)

        cv2.imshow('Final',total)
        cv2.imshow('Fondo', fondo)

        cv2.imshow('Captura',frame)
        
        if cv2.waitKey(1) & 0xFF==ord('c'):
            fondo=cv2.imread('./fondo2.jpg')
            fondo=cv2.resize(fondo,(640,480))
        
        if cv2.waitKey(1) & 0xFF==ord('b'):
            fondo=cv2.imread('./fondo1.jpg')
            fondo=cv2.resize(fondo,(640,480))
        
        exportable.write(total)
            
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
        
video.release()
exportable.release()
cv2.destroyAllWindows()