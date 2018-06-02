# Reading complex list from firebase

import pyrebase

# configuring your firebase database

config = {

  # Credentials taken from Firebase 'Web Setup' 

  "apiKey": "AIzaSyD2UCfuM-iFiMBKBT9uHfeSuNct5b-a4Wc",
  "authDomain": "city-tour-guide-5f8f0.firebaseapp.com",
  "databaseURL": "https://city-tour-guide-5f8f0.firebaseio.com",
  "storageBucket": "city-tour-guide-5f8f0.appspot.com"
}

# initialize the firebase object
firebase = pyrebase.initialize_app(config)

# get reference of database from firebase object
fb = firebase.database()

# fetching data of 'Students-List' child node into result variable
result = fb.child("students-list").get()
i=0

# a for-each loop to extract the result of every child.
# get() method will get the object key
# val() method will get the object value

for student in result.each():
    print(fb.child("students-list").child(i).child("name").get().val())
    print(fb.child("students-list").child(i).child("course").get().val())
    print(fb.child("students-list").child(i).child("fees-paid").get().val())
    print("**************")
    i = i+1
