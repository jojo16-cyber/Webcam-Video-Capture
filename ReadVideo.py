import cv2
cap = cv2.VideoCapture("C:\\Users\\khushbu\\Downloads\\WhatsApp Video 2024-12-24 at 12.48.12_84557c3b.mp4")
print("Video Captured",cap)
while True:
    ret,frame = cap.read() # ret is an boolean variable
    frame = cv2.resize(frame,(600,700))
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # This line converts whole video to gray color video
    cv2.imshow("frame",frame)
    cv2.imshow("Gray frame", gray)
    k = cv2.waitKey(25) # 25 is number of frames passing at a time. 25 is normal playback speed.
    # if we reduce number than 25 then speed of video increases.
    if k == ord("s") & 0xFF: # 0xFF is used when error occurs.Not Necessary.
        break
cap.release()
cv2.destroyAllWindows()    