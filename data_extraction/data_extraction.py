import cv2
 
 # Opens the Video file
 #if u want to collect the sample from live stream then pass 0
cap= cv2.VideoCapture('fire.mp4')
i=1
j=0
k=0

while(cap.isOpened()):

    ret, frame = cap.read()
   
    if ret == False:
        break
    res =cv2.resize(frame,(180,120))   
   # cv2.imshow(,res)  
   # extract every 30th frame..      
    if i%30 == 0:
        # this program end when it collect the 4500 sample
        if k!=4500:
            cv2.imwrite('Fire'+str(j)+'.jpg',res)
            j+=1
            k+=1    
    i+=1
 
cap.release()
cv2.destroyAllWindows()