import cvzone
import cv2

from cvzone.FaceMeshModule import FaceMeshDetector

cap=cv2.VideoCapture(0)

cap.set(3,1200)
cap.set(4,700)


detc=FaceMeshDetector(maxFaces=1)

while True:

    _,frame=cap.read()
    frame,face=detc.findFaceMesh(frame)

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == ord("s"):
        break

cap.release()
cv2.destroyAllWindows()