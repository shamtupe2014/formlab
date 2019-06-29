from . import views
from django.urls import path


urlpatterns = [
    path('',views.webhome,name="webhome"),
    path('signup/',views.signup,name="signup"),
    path('display/',views.display,name="display"),
    path('register/',views.register,name="register"),
    path('login/',views.login,name="login"),
    path('mpsc/',views.mpsc,name="mpsc"),
    path('enter/',views.enter,name="enter"),
    path('file/',views.file,name="file")

]
