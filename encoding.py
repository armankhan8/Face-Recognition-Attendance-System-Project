import cv2
import face_recognition
import os
import pickle
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':"https://facerecognitionattendancerealt-default-rtdb.firebaseio.com/",
    'storageBucket': "facerecognitionattendancerealt.appspot.com"
})

# Graphics A
folderPath = 'Images'
list = os.listdir(folderPath)

# print(list)
ImgList = []
studentIds = []

for path in list:
    ImgList.append(cv2.imread(os.path.join(folderPath, path)))
    # For append only ids of student with first index
    studentIds.append(os.path.splitext(path)[0])
    # print(os.path.splitext(path)[0])

    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)


print(studentIds)

# function for used encode/color
def findEncodings(Ilist):
    encodeList = []
    for img in Ilist:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]  # Changed here
        encodeList.append(encode)

    return encodeList

print("Encoding Started ...")
encodeListKnown = findEncodings(ImgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")

# How many Image Present 
# print(len(ImageList))
