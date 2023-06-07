import cv2
import urllib.request
from cvzone.HandTrackingModule import HandDetector
detector = HandDetector(maxHands =1, detectionCon=0.8)

cap = cv2.VideoCapture(0)

while True:
    ret, photo = cap.read()
    hand = detector.findHands(photo,draw=False)
    
    if hand :
        detectHand = hand[0]
        if detectHand:
            fingerup = detector.fingersUp(detectHand)
            if detectHand['type'] == 'Right':
                
                if fingerup == [1, 0, 0, 0, 0]:
                    print("Thumbs up one container launched ")
                    for i in range(1):
                        request_url = urllib.request.urlopen('https://nmkuctsia0.execute-api.ap-south-1.amazonaws.com/test/docker')
                        print(request_url.read())
                
                
                elif fingerup == [0, 1, 0, 0, 0]:
                    print("one finger up : one container launched")    
                    for i in range(1):
                        request_url = urllib.request.urlopen('https://nmkuctsia0.execute-api.ap-south-1.amazonaws.com/test/docker')
                        print(request_url.read())
                
                
                elif fingerup == [1,1,0,0,0]:
                    print("Two finger up : two container launched")
                    for i in range(2):
                        request_url = urllib.request.urlopen('https://nmkuctsia0.execute-api.ap-south-1.amazonaws.com/test/docker')
                        print(request_url.read())
                
                
                elif fingerup == [1,1,1,0,0]:
                    print("three finger up : three container launched  ")
                    for i in range(3):
                        request_url = urllib.request.urlopen('https://nmkuctsia0.execute-api.ap-south-1.amazonaws.com/test/docker')
                        print(request_url.read())
                
                
                elif fingerup == [1,1,1,1,0]:
                    print("four finger : four containers launched")
                    for i in range(4):
                        request_url = urllib.request.urlopen('https://nmkuctsia0.execute-api.ap-south-1.amazonaws.com/test/docker')
                        print(request_url.read())
                
                
                elif fingerup == [1,1,1,1,1]:
                    print("all five fingers up : five container launched")
                    for i in range(5):
                        request_url = urllib.request.urlopen('https://nmkuctsia0.execute-api.ap-south-1.amazonaws.com/test/docker')
                        print(request_url.read())
               
                
                elif fingerup ==  [0,1,1,0,0]:
                    print("index and middle finger : two container launched")
                    for i in range(2):
                        request_url = urllib.request.urlopen('https://nmkuctsia0.execute-api.ap-south-1.amazonaws.com/test/docker')
                        print(request_url.read())
                
                
               
                elif fingerup == [0,1,1,1,0]:
                    print("middle three fingers up : threee container launched")
                    for i in range(3):
                        request_url = urllib.request.urlopen('https://nmkuctsia0.execute-api.ap-south-1.amazonaws.com/test/docker')
                        print(request_url.read())
            else:
                
                if fingerup == [1, 0, 0, 0, 0]:
                    print("Thumbs up one container launched ")
                    for i in range(1):
                        request_url = urllib.request.urlopen('https://nmkuctsia0.execute-api.ap-south-1.amazonaws.com/test/removedocker')
                        print(request_url.read())
                
                
                elif fingerup == [0, 1, 0, 0, 0]:
                    print("one finger up : one container launched")    
                    for i in range(1):
                        request_url = urllib.request.urlopen('https://nmkuctsia0.execute-api.ap-south-1.amazonaws.com/test/removedocker')
                        print(request_url.read())
                
                
                elif fingerup == [1,1,0,0,0]:
                    print("Two finger up : two container launched")
                    for i in range(2):
                        request_url = urllib.request.urlopen('https://nmkuctsia0.execute-api.ap-south-1.amazonaws.com/test/removedocker')
                        print(request_url.read())
                
                
                elif fingerup == [1,1,1,0,0]:
                    print("three finger up : three container launched  ")
                    for i in range(3):
                        request_url = urllib.request.urlopen('https://nmkuctsia0.execute-api.ap-south-1.amazonaws.com/test/removedocker')
                        print(request_url.read())
                
                
                elif fingerup == [1,1,1,1,0]:
                    print("four finger : four containers launched")
                    for i in range(4):
                        request_url = urllib.request.urlopen('https://nmkuctsia0.execute-api.ap-south-1.amazonaws.com/test/removedocker')
                        print(request_url.read())
                
                
                elif fingerup == [1,1,1,1,1]:
                    print("all five fingers up : five container launched")
                    for i in range(5):
                        request_url = urllib.request.urlopen('https://nmkuctsia0.execute-api.ap-south-1.amazonaws.com/test/removedocker')
                        print(request_url.read())
               
                
                elif fingerup ==  [0,1,1,0,0]:
                    print("index and middle finger : two container launched")
                    for i in range(2):
                        request_url = urllib.request.urlopen('https://nmkuctsia0.execute-api.ap-south-1.amazonaws.com/test/removedocker')
                        print(request_url.read())
                
                
               
                elif fingerup == [0,1,1,1,0]:
                    print("middle three fingers up : threee container launched")
                    for i in range(3):
                        request_url = urllib.request.urlopen('https://nmkuctsia0.execute-api.ap-south-1.amazonaws.com/test/removedocker')
                        print(request_url.read())
                
                
                
        
    
    cv2.imshow("my photo", photo)
    if  cv2.waitKey(10) == 13:
        break
        
cv2.destroyAllWindows()
