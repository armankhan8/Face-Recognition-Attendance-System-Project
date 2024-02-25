import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':"https://facerecognitionattendancerealt-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "321654": {
        "name": "Arman Khan",
        "major": "B.Tech",
        "starting_year": 2022,
        "total_attendance": 5,
        "standing":"G",
        "year": 2,
        "last_Attendance_time": "2024-2-15 12:12:34"
    },
        "852741": {
        "name": "Nadeem",
        "major": "MBA",
        "starting_year": 2023,
        "total_attendance": 6,
        "standing":"G",
        "year": 1,
        "last_Attendance_time": "2024-12-01 12:34:34"
    },
        "963852": {
        "name": "Elon Musk",
        "major": "Physics",
        "starting_year": 2015,
        "total_attendance": 1,
        "standing":"G",
        "year": 1,
        "last_Attendance_time": "2015-2-15 11:12:34"
    },

}

for key, value in data.items():
    ref.child(key).set(value)