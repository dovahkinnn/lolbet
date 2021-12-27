
from requests import request
from django.http.response import HttpResponse
from django.shortcuts import render
import pyrebase
# Create your views here.
config = {
  "apiKey": "AIzaSyAwH2uSz9iiUTBa8W4NMf-3Osu7spMmbz4",
  "authDomain": "django-c0d88.firebaseapp.com",
  "projectId": "django-c0d88",
  "storageBucket": "django-c0d88.appspot.com",
  "messagingSenderId": "290546126178",
  "appId": "1:290546126178:web:68e8cefcd33dbf6259b03b",
  "measurementId": "G-F5G1043X39",
  "databaseURL": "https://django-c0d88-default-rtdb.firebaseio.com",
}

firebase=pyrebase.initialize_app(config)
auth=firebase.auth()
db=firebase.database()
def index(request):
    return render(request,"html/index.html")
def login(request):
    return render(request,"html/login.html")


def anasayfa(request):
    name=request.POST.get('isim','')
    email=request.POST.get('email','')
    password=request.POST.get('password','')
    user = auth.create_user_with_email_and_password(email, password) 
    print(user)
    id_token=user["idToken"]
    # auth.send_email_verification(id_token)
    
    data = {"name": name,"email":email,"password":password,"id":"2"}
    db.child("users").child("2").set(data)
    return render(request,"html/user.html",{"name":name})
    

def signin(request):
  email=request.POST.get('email','')
  password=request.POST.get('password','')
  auth.sign_in_with_email_and_password(email,password)
  
  return render(request,"html/merhaba.html",{"email":email})




