import cv2
import os
for filename in os.listdir('test'):
    img = cv2.imread('test/' + filename)
    if img is None:
        print("Error: Image not loaded.")
        exit()
    car_cascade = cv2.CascadeClassifier('model/cascade_2.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, scaleFactor=7, minNeighbors=5)
    for (x, y, w, h) in cars:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("Car Detection", img)
    cv2.waitKey(0)
cv2.destroyAllWindows()