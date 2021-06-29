import cv2
import glob
import os

list_of_files = glob.glob('cropped_face/*') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getmtime)

i = latest_file.split("#")[1]

# print(i)
def detect(detctor):
    face_cascade = cv2.CascadeClassifier(detctor)
    cap = cv2.VideoCapture(0) 
    while True:
        _, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            cropped_face = img[y:y+h, x:x+w]
            cv2.imwrite(f"cropped_face/img#{int(i)+ 1}#.jpg",cropped_face)
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.imshow('img', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


