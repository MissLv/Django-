import hashlib
import re

from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import *
from hashlib import sha1

def register(request):
    return render(request,'usermode/register.html')

def register_handle(request):
    post=request.POST
    uname=post.get('user_name')
    upwd=post.get('pwd')
    upwd2=post.get('cpwd')
    uemail=post.get('email')
    if upwd2 != upwd:
        return redirect('/usermode/register/')

    s1=sha1()
    s1.update(upwd.encode('utf-8'))
    upwd3=s1.hexdigest()

    user=UserInfo()
    user.uname=uname
    user.upwd=upwd3
    user.uemail=uemail
    user.save()
    # 注册成功，转到登录界面
    return redirect('/usermode/login')

def login(request):
    return render(request,'usermode/login.html')

def login_check(request):
    post=request.POST
    name=post.get('username')
    pwd=post.get('pwd')
    refer=post.get('refer')
    a = sha1()
    a.update(pwd.encode('utf-8'))
    a=a.hexdigest()
    list1=UserInfo.objects.filter(uname=name)
    if list1[0].upwd==a:
        request.session['uname'] = name
        request.session.set_expiry(0)
        if refer!='':
            href=re.search(r'register',refer)
            try:
                href.group()
            except AttributeError:
                return redirect(refer)
            else:
                return redirect('/usermode/user_center_info/')
        else:
            return redirect('/usermode/user_center_info/')
    else:
        context = {'login':'error'}
        return render(request,'usermode/login.html',context)

def user_center_info(request):
    name=request.session.get('uname',None)
    print(name)
    if name!=None:
        a=UserInfo.objects.filter(uname=name)
        if a.exists()==True:
            context={'status':'login','user':a[0],'pageName':'用户中心'}
            return render(request,'usermode/user_center_info.html',context)
        else:
            del request.session['uname']
            return redirect('/GoodsShow/')
    else:
        return redirect('/GoodShow/')

def user_center_site(request):
    name = request.session.get('uname', None)
    if name!=None:
        a=UserInfo.objects.filter(isDelete=False,uname=name)
        if a.exists()==True:
            userAddr=a[0].useraddress_set
            defaultAddr=userAddr.filter(ustaue=True)
            addrList = userAddr.all()
            shenlist = AreaInfo.objects.filter(aParent_id__isnull=True)
            city = City.objects.filter(aParent_id__isnull=True)
            if addrList.count()!=0:
                if defaultAddr.count() == 0:
                    defaultAddress = 'no'
                else:
                    defaultAddress = defaultAddr[0]

                context={'statu':'login','user':a[0],'useraddress':addrList,'defaultAddress':defaultAddress,'pageName':'用户中心','has_addrList':'yes','shenlist':shenlist,'city':city}
                return render(request, 'usermode/user_center_site.html', context)
            else:
                context={'has_addrList':'no','pageName':'用户中心','shenlist':shenlist,'city':city}
                return render(request, 'usermode/user_center_site.html',context)
        else:
            del request.session['uname']
            return redirect('/GoodsShow/')
    else:
        return redirect('/GoodsShow/')

def register_checkname(request):
    uname=request.GET['uname']
    a=UserInfo.objects.filter(isDelete=False,uname=uname)
    if a.count()==0:
        b='yes'
    else:
        b='no'
    return JsonResponse({'isOnly':b})

def addr_save(request):
    name = request.session.get('uname',None)
    if name != None:
        a = UserInfo.objects.filter(isDelete=False,uname=name)
        if a.exists() == True:
            uname = request.GET['username']
            proid = request.GET['pro']
            cityid = request.GET['city']
            disid = request.GET['dis']
            uaddr = request.GET['useraddress']
            ucode = request.GET['ucode']
            uphone = request.GET['uphone']
            user_id = a[0].id

            pro = AreaInfo.objects.get(pk=int(proid)).atitle
            city = AreaInfo.objects.get(pk=int(cityid)).atitle
            dis = AreaInfo.objects.get(pk=int(disid)).atitle

            useraddr = UserAddress()
            useraddr.userName = uname
            useraddr.uaddress = pro + city + dis + uaddr
            useraddr.uphone = uphone
            useraddr.ucode = ucode
            useraddr.user_id = user_id
            useraddr.ustaue = False
            useraddr.save()
            return JsonResponse({'success': 'ok'})
        else:
            del request.session['uname']
            return JsonResponse({'success': 'no'})
    else:
        return JsonResponse({'success': 'no'})

def changeDefaultAddr(request):
    id1=request.GET['id1']
    name = request.session.get('uname', None)
    if name != None:
        a = UserInfo.objects.filter(isDelete=False, uname=name)
        if a.exists() == True:
            userAddr = a[0].useraddress_set
            addrList = userAddr.all()
            for x in addrList:
                x.ustaue=False
                if x.id==int(id1):
                    x.ustaue = True
                    b=x
                x.save()
            return JsonResponse({'name':b.userName,'addr':b.uaddress,'tel':b.uphone})
        else:
            del request.session['uname']
            return redirect('/GoodsShow/')
    else:
        return redirect('/GoodsShow/')
def exchangelogin(request):
    if request.session.has_key('uname'):
        del request.session['uname']
    return redirect('/usermode/login/')

def exit(request):
    if request.session.has_key('uname'):
        del request.session['uname']
    return redirect('/GoodsShow/')
def forgetpwd(request):
    context={'pageName':'安全中心'}
    return render(request,'usermode/user_center_forgetpwd.html',context)
def forgetpwd_handle(request):
    name=request.POST['uname']
    email= request.POST['email']

    list=UserInfo.objects.filter(isDelete=False,uname=name)
    if list.count()!=0:
        if list[0].uemail==email:
            context={'name':list[0].uname,'pageName':'安全中心'}
            return render(request,'usermode/resetpwd.html',context)
        else:
            context = {'err':'pwd','pageName':'安全中心'}
            return render(request, 'usermode/misspwd.html',context)
    else:
        context = {'err': 'name','pageName':'安全中心'}
        return render(request, 'usermode/misspwd.html', context)
def resetpwd_handle(request):
    name=request.POST['name']
    pwd= request.POST['pwd']

    a=hashlib.sha1()
    a.update(pwd.encode("utf8"))
    a=a.hexdigest()

    list = UserInfo.objects.filter(isDelete=False, uname=name)[0]
    list.upwd=a
    list.save()

    request.session['uname'] = name
    request.session.set_expiry(0)

    context={'user':list,'pageName':'安全中心'}
    return render(request,'usermode/changepwdsucess.html',context)
def getshi(request,pid):
    proList = AreaInfo.objects.filter(aParent_id=int(pid))
    proList1 = []
    for x in proList:
        proList1.append([x.id, x.atitle])
    return JsonResponse({'list': proList1})

def getuseraddr(request):
    name = request.session.get('uname', None)
    if name != None:
        a = UserInfo.objects.filter(isDelete=False, uname=name)
        if a.exists() == True:
            userAddr = a[0].useraddress_set.all()
            userAddr1=[]
            for x in userAddr:
                userAddr1.append([x.id,x.uaddress,x.userName,x.uphone])
            return JsonResponse({'addrList':userAddr1,'success':'ok'})
        else:
            del request.session['uname']
            return JsonResponse({'success':'no'})
    else:
        return JsonResponse({'success':'no'})
