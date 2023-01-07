import cv2
import numpy as np

# Load the Haar cascades XML file for hand detection
hand_cascade = cv2.CascadeClassifier('haarcascade_hand.xml')

# Start the video capture
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect hands in the frame
    hands = hand_cascade.detectMultiScale(gray, 1.3, 5)
    
    # Iterate over the detected hands
    for (x,y,w,h) in hands:
        # Draw a rectangle around the hand
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        
    # Display the resulting frame
    cv2.imshow('Hand Detection', frame)
    
    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
