import cv2  #opencv - use as cv2 in python.

img1 = cv2.imread("C:\\Users\\khushbu\\Downloads\\pexels-8moments-1266810.jpg")
# img1 = cv2.imread("C:\\Users\\khushbu\\Downloads\\pexels-8moments-1266810.jpg",1) is same where 1 indicates color image which is by default.
img1 = cv2.resize(img1,(1280,700)) # width,height
print(img1)
cv2.imshow("original - 3D Array",img1)
img1 = cv2.flip(img1,0) 
#In flip, whwn 0 is passed it flip upside down, when 1 is passed it flips left to right and when flipped -1 it flips bith upside down and left to right.
cv2.imshow("Flipped Image - 3D Array",img1)

# Image in gray scale mode
img2 = cv2.imread("C:\\Users\\khushbu\\Downloads\\pexels-8moments-1266810.jpg",0)
# img1 = cv2.imread("C:\\Users\\khushbu\\Downloads\\pexels-8moments-1266810.jpg",0) where 0 indicates image in grayscale mode.
img2 = cv2.resize(img2,(1300,720)) # width,height
print("GrayScale Image =>/n", img2)
cv2.imshow("gray scale image - 2D Array",img2)

# Image in unchanged mode that is color saturation is more.It has more color values or it has  more alpha channels.
img2 = cv2.imread("C:\\Users\\khushbu\\Downloads\\pexels-8moments-1266810.jpg",-1)
# img1 = cv2.imread("C:\\Users\\khushbu\\Downloads\\pexels-8moments-1266810.jpg",-1) where 0 indicates image in unchanged mode.
img2 = cv2.resize(img2,(1500,750)) # width,height
print("Unchanged Image =>/n", img2)
cv2.imshow("Unchanged Image - 3D Array",img2)

cv2.waitKey()
# cv2.waitKey() is equal to cv2.waitKey(0). Here cv2.waitKey(3000) shows image for 3 seconds.
cv2.destroyAllWindows()
