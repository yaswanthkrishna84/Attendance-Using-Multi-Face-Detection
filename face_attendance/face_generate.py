from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2
import h5py
import _pickle as cPickle
import os

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the (optional) video file")
args = vars(ap.parse_args())
number = 0
frame_count = 0
detector = dlib.get_frontal_face_detector()
print("enter the person name")
name = input()
folder_name = "dataset/" + name
if os.path.exists(folder_name):
    print("Folder exist")
else:
    os.makedirs(folder_name)
if not args.get("video", False):
    camera = cv2.VideoCapture(0)
else:
    camera = cv2.VideoCapture(args["video"])
while True:
    if frame_count % 5 == 0:
        print("keyframe")
        (grabbed, image) = camera.read()
        if args.get("video") and not grabbed:
            break
        image = imutils.resize(image, width=500)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        rects = detector(gray, 1)
        for i, rect in enumerate(rects):
            (x, y, w, h) = face_utils.rect_to_bb(rect)
            cro = image[y : y + h, x : x + w]
            out_image = cv2.resize(cro, (108, 108))
            fram = os.path.join(folder_name + "/", str(number) + "." + "jpg")
            number += 1
            cv2.imwrite(fram, out_image)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        frame_count += 1
    else:
        frame_count += 1
        print("redudant frame")
    if number > 51:
        break
    cv2.imshow("output image", image)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
camera.release()
cv2.destroyAllWindows()
