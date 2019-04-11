import pyrebase

config = {
    "apiKey": "AIzaSyA7UeCzU9zPXV4O1uJq6-GUjn80o-HlFP4",
    "authDomain": "todo-1b3e4.firebaseapp.com",
    "databaseURL": "https://todo-1b3e4.firebaseio.com",
    "projectId": "todo-1b3e4",
    "storageBucket": "todo-1b3e4.appspot.com",
    "messagingSenderId": "1013535024489"
    };

class DB:
    
    
    def __init__(self):
        self.firebase = pyrebase.initialize_app(config)


    def addToDo(self,task,description):               
        data = {"task": task, "description": description}
        db = self.firebase.database()
        db.child("tasks").push(data)

    def get_all(self):
        db = self.firebase.database()
        return db.child("tasks").get()
