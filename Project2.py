# Break video into Multiple Images and Store in a folder
import cv2

#capture video
videocap = cv2.VideoCapture("C:\\Users\\prati\\Downloads\\OpenCV\\hell.mp4")
ret, image = videocap.read() #Read the video
# we are writing this outside the while loop basicallt we
#want to capture all the images 
# it breaks the video into frames

count =0
while True:
	if ret == True:
		cv2.imwrite('C:\\Users\\prati\\Downloads\\OpenCV\\frames\\imgN%d.jpg'%count,image)
		# we have written % so that every image will be saved with it's unique name
		videocap.set(cv2.CAP_PROP_POS_MSEC,(count**100))
		#this is to capture at which speed
		ret, image = videocap.read()#we need to capture here too
		# so that we can get infinite looping over the frames
		cv2.imshow("res",image)

		count += 1
		if cv2.waitKey(1) & 0xFF == ord("q"):
			break
			cv2.destroyAllWindows()
	else:
		break
videocap.release()
cv2.destroyAllWindows()



