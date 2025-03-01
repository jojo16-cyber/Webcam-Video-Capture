# Capture video from webcam and save into memory.
import cv2
cap = cv2.VideoCapture(0) # here 0 is used to capture video from internal camera of laptop and 1 is used to capture video from external camera.

# Code to save output
#DIVX,XVID,MJPG,X264,WMV1,WMV2
fourcc = cv2.VideoWriter_fourcc(*"XVID")
# It contains 4 output name,codec,fps,resolution
output1 = cv2.VideoWriter("C:\\Users\\khushbu\\Downloads\\Output1.avi",fourcc,20.0,(640,480)) 
output2 = cv2.VideoWriter("C:\\Users\\khushbu\\Downloads\\Output2.avi",fourcc,20.0,(640,480),0) # 0 tells gray scale mode
while cap.isOpened():  # Capture fram till camera is opened.
    ret,frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # frame = cv2.flip(frame,0) can also be used.
        cv2.imshow("frame",frame)
        cv2.imshow("gray",gray)
        output1.write(frame)
        output2.write(gray)
        if cv2.waitKey(1) & 0xFF == ord("s"): # waitKey(1) indicates video and waitKey(0) indicates image.
            break
cap.release()
output1.release()
output2.release()
cv2.destroyAllWindows()        