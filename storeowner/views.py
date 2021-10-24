from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, logout, login
from .models import *
from django.utils.datastructures import MultiValueDictKeyError



# Create your views here.
def stores(request):
    items=StoreInfo.objects.all()

    return render(request, 'stores.html', {'items':items})

def book_library(request,storename):
    storename=storename
    items=BookInfo.objects.all().filter(storename=storename)
    seller=StoreInfo.objects.all().filter(storename=storename)

    
    return render(request, 'book_library.html', {'items':items, 'storename':storename, 'seller':seller})

def bookform(request, storename):
    if request.user.is_authenticated:
        store_name=storename
        user=request.user
        if request.method=='POST':
            username=user.username
            storename=store_name
            bookid=request.POST['bookid']
            bookname=request.POST['bookname']
            bookprice=request.POST['bookprice']
            bookauthor=request.POST['bookauthor']
            bookimage=request.FILES['bookimage']

            b_info=BookInfo(username=username, storename=storename, bookid=bookid, bookname=bookname, bookprice=bookprice, bookauthor=bookauthor, bookimage=bookimage)
            b_info.save()
            return redirect("/bookform{{storename}}")
        return render(request, 'book_form.html', {'user':user, 'store_name':storename})
    else:
        note='You must log in first'
        return render(request, 'login_s.html',{'note':note})
    
    

def storeform(request):
    if request.user.is_authenticated:
        user=request.user
        if request.method=='POST':
            username=user.username
            storename=request.POST['storename']
            totalbooks=request.POST['totalbooks']
            storeimage=request.FILES['storeimage']
            rating=request.POST['rating']
            first_name=user.first_name
            last_name=user.last_name

            s_info=StoreInfo(username=username, storename=storename, totalbooks=totalbooks, storeimage=storeimage, rating=rating, first_name=first_name, last_name=last_name)
            s_info.save()
        return render(request, 'store_form.html', {'user':user})
    
    return render(request, 'store_form.html')

def books_list(request):
    return HttpResponse('Books List')

def login_seller(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            note= 'login successfully'
            return redirect('/')
        else:
            return render(request, 'login_s.html')
    else:
        return render(request, 'login_s.html')

def logout_seller(request):
    logout(request)
    return redirect('/login_seller')

def register_seller(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                note='User Already Exist'
                return render (request,'register_s.html',{'note':note})
            elif User.objects.filter(email=email).exists():
                note='user Already Exist with this email'
                return render (request,'register_s.html',{'note':note})

            else:
                u_info=User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password1)
                u_info.save()
                note='Registration successful'
                return render (request,'login_s.html',{'note':note})


        else:
            note='Passwords not matching'
            return render(request, 'register_s.html',{'note':note})

    return render(request, 'register_s.html')


def book_update(request, bookid):
    
    item=BookInfo.objects.filter(bookid=bookid)
    print(item)
    for i in item:
        if request.user.is_authenticated:
            
            if request.method=='POST':
                username=i.username
                storename=i.storename
                bookid=request.POST['bookid']
                bookname=request.POST['bookname']
                bookprice=request.POST['bookprice']
                bookauthor=request.POST['bookauthor']
                
                try:
                    image=request.FILES['bookimage']
                except MultiValueDictKeyError:
                    image=False
                    
                
                b_info=BookInfo(username=username, storename=storename, bookid=bookid, bookname=bookname, bookprice=bookprice, bookauthor=bookauthor, bookimage=i.bookimage)
                b_info.save()
                note = 'Updated successfully'
                return redirect('/book_library<str:storename>')

            
    return render(request, 'book_update.html', {'item':item})

def book_delete(request, bookid):
    item=BookInfo.objects.filter(bookid=bookid)
    item.delete()
    note='Deleted successfully'
    return redirect('/book_library<str:storename>')

