from django.shortcuts import render,redirect
from userapp.models import Userdb,postsdb,followersdb,likes,commentdb
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError



# Create your views here.
def login(req):
    return render(req,'loginpage.html')

def saveuser(req):
    if req.method=="POST":
        na=req.POST.get('name')
        us=req.POST.get('username')
        ps=req.POST.get('password')
        ps1=req.POST.get('password1')
        ge=req.POST.get('radio')
        em=req.POST.get('email')
        dp=req.FILES['dispic']
        cp=req.FILES['covpic']
        if ps==ps1:
            if Userdb.objects.filter(Username=us).exists():
                messages.info(req, 'Username already Exists')
                return redirect(login)
            elif Userdb.objects.filter(Email=em).exists():
                messages.info(req,'Email already registered')
                return redirect(login)
            else:
                obj = Userdb(Name=na, Username=us, Password=ps, Gender=ge, Email=em, Profile=dp, Cover=cp)
                obj.save()
                messages.success(req, "Congratulations..! welcome to PHOTTOSSY.. please login with your credentials")
                return redirect(login)
        else:
            messages.info(req, 'Password doesnot match')
            return redirect(login)

def loginuser(req):
    if req.method=="POST":
        usrnme=req.POST.get('usern')
        psswrd=req.POST.get('pswrd')
        if Userdb.objects.filter(Username=usrnme,Password=psswrd).exists():
            req.session['username']=usrnme
            req.session['Password']=psswrd
            return redirect(homepage)
        else:
            messages.info(req, "Invalid Credentials..!")
            return redirect(login)
    else:
        return redirect(login)

def logoutuser(req):
    del req.session['username']
    del req.session['Password']
    return redirect(login)

def profiletimeline(req):
    prof = Userdb.objects.get(Username=req.session['username'])
    count = followersdb.objects.filter(Follower=prof.id).count()
    post=postsdb.objects.filter(Username_id=prof.id)
    follower = followersdb.objects.filter(Username=req.session['username']).count()
    following = followersdb.objects.filter(Username=req.session['username'])
    users = Userdb.objects.all()
    return render(req,'timeline.html', {'prof': prof, 'count': count, 'post': post, 'follower':follower, 'following':following, 'users':users})

def saveposts(req):
    if req.method=="POST":
        img=req.FILES['posts']
        user=Userdb.objects.get(Username=req.session['username'])
        txt=req.POST.get('text')
        pst=postsdb(Username=user,Posts=img,Caption=txt)
        pst.save()
        return redirect(homepage)

def homepage(req):
    prof = Userdb.objects.get(Username=req.session['username'])
    post=postsdb.objects.all()
    users=Userdb.objects.all()
    like= likes.objects.filter(Username=req.session['username'])
    follower=followersdb.objects.filter(Username=req.session['username'])
    return render(req,'homepage.html', {'prof': prof, 'post': post, 'users':users, 'follower':follower, 'like':like })

def userprofile(req,dataid):
    data=Userdb.objects.get(id=dataid)
    post=postsdb.objects.filter(Username_id=dataid)
    count=followersdb.objects.filter(Follower=dataid).count()
    follower = followersdb.objects.filter(Username=data.Username).count()
    following = followersdb.objects.filter(Username=req.session['username'])
    users = Userdb.objects.all()
    prof = Userdb.objects.get(Username=req.session['username'])
    if followersdb.objects.filter(Follower=dataid,Username=req.session['username']).exists():
        button="Unfollow"
    else:
        button="Follow"
    return render(req,'userstimeline.html' , {'data':data, 'post':post, 'button':button,'count':count, 'follower':follower, 'following':following, 'users':users, 'prof':prof})

def addfollower(req,dataid):
    follower=Userdb.objects.get(id=dataid)
    User=Userdb.objects.get(Username=req.session['username'])
    obj=followersdb(Follower=follower,Username=User)
    obj.save()
    messages.success(req, "Following")
    return redirect(userprofile,dataid)

def removefollower(req,dataid):
    obj=followersdb.objects.filter(Follower_id=dataid,Username=req.session['username'])
    obj.delete()
    messages.info(req, "Unfollowed")
    return redirect(userprofile,dataid)

def addlike(req,dataid,postid):
    user=Userdb.objects.get(Username=req.session['username'])
    post=postsdb.objects.get(id=postid)
    like=likes.objects.filter(Username=user.Username,post=post.id).first()
    if like == None:
        obj=likes(Username=user.Username,post=post.id)
        obj.save()
        post.no_of_like = post.no_of_like+1
        post.like_post(user)
        post.save()
        return redirect(homepage)
    else:
        like.delete()
        post.no_of_like = post.no_of_like-1
        post.remove_like(user)
        post.save()
        return redirect(homepage)

def search(req):
    following = followersdb.objects.filter(Username=req.session['username'])
    users = Userdb.objects.all()
    if req.method=="POST":
        query=req.POST.get('qry')
        if query:
            results=Userdb.objects.filter(Name__contains=query)
        else:
            results=[]
        return render(req, 'search.html',{'results':results, 'following':following, 'users':users})

def images(req):
    prof = Userdb.objects.get(Username=req.session['username'])
    count = followersdb.objects.filter(Follower=prof.id).count()
    post = postsdb.objects.filter(Username_id=prof.id)
    follower = followersdb.objects.filter(Username=req.session['username']).count()
    followers=followersdb.objects.filter(Username=req.session['username'])
    users = Userdb.objects.all()
    return render(req,'profileimages.html',{'prof': prof, 'count': count, 'post': post, 'follower':follower, 'followers':followers, 'users':users})

def friends(req):
    prof = Userdb.objects.get(Username=req.session['username'])
    count = followersdb.objects.filter(Follower=prof.id)
    post = postsdb.objects.filter(Username_id=prof.id)
    follower = followersdb.objects.filter(Username=req.session['username'])
    users=Userdb.objects.all()
    return render(req, 'profilefriends.html', {'prof': prof, 'count': count, 'post': post, 'follower': follower, 'users':users})

def prof(req,dataid):
    user=Userdb.objects.get(id=dataid)
    if user.Username==req.session['username']:
        return redirect(profiletimeline)
    else:
        return redirect(userprofile,dataid)

def messagess(req):
    prof = Userdb.objects.get(Username=req.session['username'])
    count = followersdb.objects.filter(Follower=prof.id).count()
    post = postsdb.objects.filter(Username_id=prof.id)
    follower = followersdb.objects.filter(Username=req.session['username']).count()
    return render(req, 'msgs.html', {'prof': prof, 'count': count, 'post': post, 'follower': follower})

def notfcn(req):
    prof = Userdb.objects.get(Username=req.session['username'])
    count = followersdb.objects.filter(Follower=prof.id).count()
    post = postsdb.objects.filter(Username_id=prof.id)
    follower = followersdb.objects.filter(Username=req.session['username']).count()
    return render(req, 'ntfcn.html', {'prof': prof, 'count': count, 'post': post, 'follower': follower})

def comments(req,dataid,postid):
    user=Userdb.objects.get(id=dataid)
    post=postsdb.objects.get(id=postid)
    comm=commentdb.objects.filter(post_id=postid)
    return render(req,'comments.html',{'user':user , 'post':post, 'comm':comm})

def savecomment(req,postid,dataid):
    user = Userdb.objects.get(Username=req.session['username'])
    post = postsdb.objects.get(id=postid)
    if req.method=="POST":
        cm=req.POST.get("comment")
        obj=commentdb(post=post,User=user,comment=cm)
        obj.save()
        return redirect(comments,dataid,postid)

def editprof(req):
    prof = Userdb.objects.get(Username=req.session['username'])
    count = followersdb.objects.filter(Follower=prof.id).count()
    post = postsdb.objects.filter(Username_id=prof.id)
    follower = followersdb.objects.filter(Username=req.session['username']).count()
    return render(req, 'editprofile.html', {'prof': prof, 'count': count, 'post': post, 'follower': follower})

def updateprof(req):
    if req.method=="POST":
        na = req.POST.get('name')
        us = req.session['username']
        ge = req.POST.get('radio')
        em = req.POST.get('email')
        try:
            dp = req.FILES['dispic']
            fs= FileSystemStorage
            prof=fs.save(dp.name,dp)
        except MultiValueDictKeyError:
            prof=Userdb.objects.get(Username=req.session['username']).Profile
        try:
            cp = req.FILES['covpic']
            fs = FileSystemStorage
            cov = fs.save(cp.name, cp)
        except MultiValueDictKeyError:
            cov=Userdb.objects.get(Username=req.session['username']).Cover
        Userdb.objects.filter(Username=req.session['username']).update(Name=na, Username=us, Gender=ge, Email=em, Profile=prof, Cover=cov)
        return redirect(profiletimeline)


