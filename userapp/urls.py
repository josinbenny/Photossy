from django.urls import path
from userapp import views

urlpatterns=[
    path('login/',views.login,name='login'),
    path('userprofile/<int:dataid>/',views.userprofile,name='userprofile'),
    path('prof/<int:dataid>/',views.prof,name='prof'),
    path('saveuser/',views.saveuser,name='saveuser'),
    path('loginuser/',views.loginuser,name='loginuser'),
    path('profiletimeline/',views.profiletimeline,name='profiletimeline'),
    path('logoutuser/',views.logoutuser,name='logoutuser'),
    path('saveposts/',views.saveposts,name='saveposts'),
    path('homepage/',views.homepage,name='homepage'),
    path('images/',views.images,name='images'),
    path('friends/',views.friends,name='friends'),
    path('comments/<int:dataid>/<postid>/',views.comments,name='comments'),
    path('messagess/',views.messagess,name='messagess'),
    path('notfcn/',views.notfcn,name='notfcn'),
    path('search/',views.search,name='search'),
    path('editprof/',views.editprof,name='editprof'),
    path('updateprof/',views.updateprof,name='updateprof'),
    path('addfollower/<int:dataid>/',views.addfollower,name='addfollower'),
    path('removefollower/<int:dataid>/',views.removefollower,name='removefollower'),
    path('addlike/<int:dataid>/<postid>/',views.addlike,name='addlike'),
    path('savecomment/<int:dataid>/<postid>/',views.savecomment,name='savecomment'),
]