import cv2
import numpy as np
from tensorflow.keras.models import load_model
model = load_model('SLT.h5')
arrays=["a","b","c","d","e","f","g","h","i","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y"]
cap = cv2.VideoCapture(0)

while(1):
        
    ret, frame = cap.read()
    frame=cv2.flip(frame,1)
    
    roi=frame[50:300, 50:300]        
    cv2.rectangle(frame,(50,50),(300,300),(0,255,0),0)    
    hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    
    hsv=cv2.resize(hsv,(28,28))
    
    hsv=np.expand_dims(np.array(hsv),axis=2)
    
    hsv=np.expand_dims(np.array(hsv),axis=0)
    
    y_predicated = model.predict(hsv)

    sonuc=y_predicated.flatten()
    a=0
    b=0
    for x in sonuc:    
        if x==1.0:
            b=a
            break
        a=a+1
        
    font = cv2.FONT_HERSHEY_SIMPLEX  

    cv2.putText(frame,arrays[b],(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
    cv2.putText(frame,"Press 'Esc' To Exit",(0,460), font, 1, (255,0,0), 2, cv2.LINE_AA)
    
    cv2.imshow('frame',frame)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    
 
cv2.destroyAllWindows()
cap.release() 
    
