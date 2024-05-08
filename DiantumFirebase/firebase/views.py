from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth

import pyrebase

# Your web app's Firebase configuration
# For Firebase JS SDK v7.20.0 and later, measurementId is optional
config = {
    "apiKey": "AIzaSyCWBAWIAMb0K-Rl8qdKllsmlj3K7wAg_vc",
    "authDomain": "diamtum-firebase.firebaseapp.com",
    "databaseURL": "https://diamtum-firebase-default-rtdb.firebaseio.com",
    "projectId": "diamtum-firebase",
    "storageBucket": "diamtum-firebase.appspot.com",
    "messagingSenderId": "304053212428",
    "appId": "1:304053212428:web:0c1e9fe26e554df5fda529",
}

# Initialize Firebase
# ====== A Pyrebase can use multiple Firebase services ======
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()  # Authentication
database = firebase.database()  # Database
store = firebase.storage()  # Store


# Create your views here.

def index(request):
    query_result = database.get().val()
    # print(query_result)
    return render(request, "index.html", {"clave": query_result})


# database.child('Alumnos').child('Nombre').get().val() para obtener todos los datos de la base de datos
# database.child().set() para agregar datos a la base de datos.


def sign(request):
    return render(request, "signIn.html")


def signIn(request):
    email = request.POST.get("email")
    password = request.POST.get("password")

    try:
        user = authe.sign_in_with_email_and_password(email, password)
        query_result = database.get().val()
        # print(query_result)
    except:
        message = "Credenciales invalidas"
        messages.error(request, message)  # Almacenar el mensaje en la sesión
        return redirect("namespacefirebase:sign")

    print(user["idToken"])
    session_id = user["idToken"]
    request.session["uid"] = str(session_id)
    # return render(request, "welcome.html", {"key": email})
    return render(request, "index.html", {"clave": query_result})


def signUp(request):
    return render(request, "signUp.html")


def signUp_register(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    password = request.POST.get("password")

    try:
        user=authe.create_user_with_email_and_password(email,password)
    except:
        message = "Credenciales invalidas"
        messages.error(request, message)  # Almacenar el mensaje en la sesión
        return redirect("namespacefirebase:sign")
    
    uid = user["localId"]  # Database of firebase
    data={"name":name, "status":"1"}
    database.child("users").child(uid).child("details").set(data)
    return render(request, "signIn.html")


def logout(request):
    auth.logout(request)
    return redirect("namespacefirebase:signIn")
