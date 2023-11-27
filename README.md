# FaceRecognitionAttendance

An Android as frontend and Python as backend face recognition app used on attendance management

#Python
#Flask
#Tensorflow
#Android
#Tenserflow-lite

# Follow These Steps

## Python - Backend

1. Create a python virtual environment
   -> `python3 -m virtualenv env`
2. Active env
   -> `source env/bin/activate`
3. Install all required library
   -> `pip install -r requirements.txt`
4. First Record face of the person using python app -
   -> `python3 face_generate.py`
   -> It will ask you to enter person name, enter and when camera open let read your face.
   -> for better result, move your face on different direction to record
5. After Record done, train dataset. It will regenerate new model with all recorded face. Face images will be on dataset named folder.
   -> `python3 face_train.py`
   -> It will create a new model file named "trained_knn_model.clf"
6. Now keep run the API
   -> `python3 face_api.py`
   -> You can modify this file as per your requirements
7. After completion of taking attendance, you have to stop the API and need to remove the duplicates from the attendance.xlsx file. For that follow below steps
   -> 1. `python3 xl_to_csv.py`
   -> 2. `python3 face_remove_duplicate.py`
   -> It will create a new file named "Final_attendance.xlsx"

## Android - Frontend

1. Change API URL on WebServices -> ConstantString.java page
2. Might be you will need to manage camera rotation if you cant see bounding box in face...
   -> Check CameraActivity.java - line 276
   -> You may need to modify as per your requirements.
   -> If face detctor will not false after detecting in DetectorActivity.java line 284 you will get result by late
   -> also because it is asynchronous and its keep calling..
   -> If result is [] , mean face not matched
   -> You need to manage flag for this.

## Output

The output will be in the form of excel sheet. The excel sheet will contain the name of the person and the time of the attendance. The excel sheet will be in the following format.
![alt text](Final_attendance.xlsx)
